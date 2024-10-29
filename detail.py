import os
import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Paths
input_folder = "./extractor/development"
output_file = "./extractor/services/development.json"

def download_image(url, save_path):
    """Download image from url and save to the specified path."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded image to {save_path}")
        return save_path.replace('./static', '')  # Remove "./static" when saving in JSON
    print(f"Failed to download image from {url}")
    return None

def scrape_data(external_link, link_last_part, category_id):
    """Scrape required data from the given external link."""
    print(f"Scraping data from {external_link}...")
    response = requests.get(external_link)
    if response.status_code != 200:
        print(f"Failed to access {external_link}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape long description
    long_description = soup.select_one("body > section.banner > div > div > div.about-header > p.about-description")
    long_description = long_description.get_text(strip=True) if long_description else None
    print("Scraped long description.")

    # Scrape website URL
    website = soup.select_one("body > section:nth-child(3) > div > div:nth-child(3) > p > a")
    website_url = website['href'] if website else None
    print("Scraped website URL.")

    # Scrape screenshots (max 2 images)
    static_image_path = f"./static/images/databases/{category_id}/{link_last_part}"
    screenshots = []
    screenshot_divs = soup.select("body > section:nth-child(4) > div > div div.browser-mockup img")[:2]
    for count, img in enumerate(screenshot_divs, 1):
        img_url = img['src']
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif not img_url.startswith('http'):
            print(f"Skipping invalid image URL: {img_url}")
            continue  # Skip invalid URLs
        
        ext = img_url.split('.')[-1]
        save_path = os.path.join(static_image_path, f"screenshot-{count}.{ext}")
        Path(os.path.dirname(save_path)).mkdir(parents=True, exist_ok=True)

        # Download image only if the URL is valid
        if img_url and img_url.lower() != 'screenshots_url':
            saved_image = download_image(img_url, save_path)
            if saved_image:
                screenshots.append(saved_image)

    print(f"Downloaded {len(screenshots)} screenshots.")

    # Scrape features
    features = []
    feature_divs = soup.select("body > section:nth-child(5) > div > div > div.benefits__cards.benefits__cards--features div.benefits__informations")
    for feature in feature_divs:
        title = feature.select_one("p.benefits__title")
        description = feature.select_one("p:not(.benefits__title)")
        features.append({
            "title": title.get_text(strip=True) if title else "",
            "description": description.get_text(strip=True) if description else ""
        })
    print(f"Scraped {len(features)} features.")

    return {
        "long_description": long_description,
        "website_url": website_url,
        "screenshots": screenshots,
        "features": features,
        "dashboard_image": screenshots[0] if screenshots else None
    }

def process_json_file(file_path, existing_ids):
    """Process each JSON file to extract and save the required data."""
    print(f"\nProcessing file: {file_path}")
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Initialize a list for the services in this file
    services = []

    for item in data:
        category = item.get("category", {})
        category_id = category.get("id")
        link_last_part = item["link"].split('/')[-1]
        external_link = item["external_link"]
        
        print(f"Processing service: {link_last_part}")

        # Check if the service ID already exists
        if link_last_part in existing_ids:
            # If it exists, add the category ID to the existing category's ids
            existing_ids[link_last_part].add(category_id)
            print(f"Service {link_last_part} already exists, adding category_id {category_id}.")
            continue
        
        scraped_data = scrape_data(external_link, link_last_part, category_id)
        if not scraped_data:
            print(f"Skipping {link_last_part} due to scraping issues.")
            continue

        output_data = {
            "category": {
                "id": category_id,
                "name": category.get("name"),
                "ids": [category_id]  # Start with the current category ID as a list
            },
            "id": link_last_part,
            "website": scraped_data["website_url"],
            "title": item["title"],
            "description": item["description"],
            "long_description": scraped_data["long_description"],
            "logo": item["logo"],
            "screenshots": scraped_data["screenshots"],
            "dashboardImage": scraped_data["dashboard_image"],
            "features": scraped_data["features"]
        }
        
        # Add the new service ID to the existing_ids dictionary with its category
        existing_ids[link_last_part] = {category_id}  # Use a set to keep unique category IDs
        services.append(output_data)

    return services

# Initialize a dictionary to hold existing service IDs
existing_ids = {}

# Process each JSON file in the input folder
all_services = []
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        services_from_file = process_json_file(os.path.join(input_folder, filename), existing_ids)
        all_services.extend(services_from_file)

# Update the existing services to include all category IDs in the ids array
for service in all_services:
    service_id = service["id"]
    if service_id in existing_ids:
        # Assign all category IDs as a list to the ids key
        service["category"]["ids"] = list(existing_ids[service_id])
    else:
        service["category"]["ids"] = []

# Save all services to a single JSON file
Path(os.path.dirname(output_file)).mkdir(parents=True, exist_ok=True)
with open(output_file, 'w') as outfile:
    json.dump(all_services, outfile, indent=4)

print(f"Saved all services to {output_file}")
