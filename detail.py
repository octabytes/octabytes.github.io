import os
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from pathlib import Path

# Paths
input_folder = "./extractor/databases"
output_folder = "./extractor/services/databases/"

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
        ext = img_url.split('.')[-1]
        save_path = os.path.join(static_image_path, f"screenshot-{count}.{ext}")
        Path(os.path.dirname(save_path)).mkdir(parents=True, exist_ok=True)
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

def process_json_file(file_path):
    """Process each JSON file to extract and save the required data."""
    print(f"\nProcessing file: {file_path}")
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    for item in data:
        category = item.get("category", {})
        category_id = category.get("id")
        link_last_part = item["link"].split('/')[-1]
        external_link = item["external_link"]
        
        print(f"Processing service: {link_last_part}")
        scraped_data = scrape_data(external_link, link_last_part, category_id)
        if not scraped_data:
            print(f"Skipping {link_last_part} due to scraping issues.")
            continue
        
        output_data = {
            "category": category,
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
        
        # Save JSON data
        output_path = os.path.join(output_folder, category_id, "services.json")
        Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as outfile:
            json.dump(output_data, outfile, indent=4)
        print(f"Saved data for {link_last_part} to {output_path}")

# Process each JSON file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        process_json_file(os.path.join(input_folder, filename))
