import os
import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

def extract_detail(service_name):
    # Paths
    input_file = f"./services/{service_name}.json"
    output_file = f"./details/{service_name}.json"

    def download_image(url, save_path):
        """Download image from url and save to the specified path."""
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded image to {save_path}")
            return save_path.replace('../static', '')  # Remove "./static" when saving in JSON
        print(f"Failed to download image from {url}")
        return None

    def scrape_data(external_link, service_id, category_id):
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
        static_image_path = f"../static/images/{service_name}/{category_id}/{service_id}"
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

    def process_json_file(file_path):
        """Process each JSON file to extract and save the required data."""
        print(f"\nProcessing file: {file_path}")
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Initialize an empty list for all services
        all_services = []

        for item in data:
            category = item.get("category", {})
            category_id = category.get("id")
            service_id = item.get("id") or item["link"].split('/')[-1]
            external_link = item["external_link"]
            
            print(f"Processing service: {service_id}")
            scraped_data = scrape_data(external_link, service_id, category_id)
            if not scraped_data:
                print(f"Skipping {service_id} due to scraping issues.")
                continue
            
            output_data = {
                "category": category,
                "id": service_id,
                "website": scraped_data["website_url"],
                "title": item["title"],
                "description": item["description"],
                "long_description": scraped_data["long_description"],
                "logo": item["logo"],
                "screenshots": scraped_data["screenshots"],
                "dashboardImage": scraped_data["dashboard_image"],
                "features": scraped_data["features"]
            }
            
            all_services.append(output_data)

        return all_services

    # Initialize a list to hold all services
    all_services = []

    services_from_file = process_json_file(input_file)
    all_services.extend(services_from_file)

    # Save all services to a single JSON file
    Path(os.path.dirname(output_file)).mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w') as outfile:
        json.dump(all_services, outfile, indent=4)

    print(f"Saved all services to {output_file}")

names = ["databases", "applications", "development", "hosting-and-infrastructure"]

for name in names:
    print("===============================================")
    print(f"              Extracting {name}               ")
    print("===============================================")

    extract_detail(name)