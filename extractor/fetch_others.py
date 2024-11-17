import os
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

SERVICE_NAME = "others" # Change this name when need check if new services exist
OUTPUT_DIR = "./services"
SERVICE_DIR = "./services"
IMAGES_DIR = "../static/images"
CATEGORY_ID = "others"
CATEGORY_NAME = "Others"

 # Ensure directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# Load all previous services
services = {}
for file_name in os.listdir(SERVICE_DIR):
    if file_name.endswith(".json"):
        with open(os.path.join(SERVICE_DIR, file_name), "r") as f:
            data = json.load(f)
            for entry in data:
                services[entry["id"]] = (entry)

services_list = ["databases", "applications", "development", "hosting-and-infrastructure"]
new_services = {}

for single_service in services_list:
    external_link = f"https://elest.io/fully-managed-services/{single_service}"

    response = requests.get(external_link)
    response.encoding = 'utf-8'
    if response.status_code != 200:
        print(f"Failed to fetch {external_link}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    cards_container = soup.select_one("#cards") or soup.find("div", id="cards")

    if not cards_container:
        print(f"No #cards container found for {external_link}")
        continue

    for a_tag in cards_container.find_all("a", href=True, class_="card-container"):
        href = a_tag["href"].strip("/")
        service_id = href.split('/')[-1]

        if service_id in services:
            continue
        else:
            print("New service found", service_id)

        link = f"/{single_service}/{CATEGORY_ID}/{service_id}"
        ext_link = urljoin("https://elest.io/", href)
        title = a_tag.select_one(".template__header > .template__label").text.strip()
        description = a_tag.select_one(".template__description").text.strip()

        # Process logo
        logo_tag = a_tag.select_one(".template__image--img img")
        if not logo_tag or not logo_tag["src"]:
            print(f"No logo image found for {ext_link}")
            continue

        logo_url = urljoin(external_link, logo_tag["src"])
        logo_ext = os.path.splitext(urlparse(logo_url).path)[-1]
        logo_path = f"{IMAGES_DIR}/{single_service}/{CATEGORY_ID}/{service_id}"
        os.makedirs(logo_path, exist_ok=True)
        logo_filename = f"{logo_path}/logo{logo_ext}"

        # Download the logo image
        # logo_response = requests.get(logo_url, stream=True)
        # if logo_response.status_code == 200:
        #     with open(logo_filename, "wb") as img_file:
        #         img_file.write(logo_response.content)
        #     logo_path_relative = logo_filename.replace("../static", "")
        # else:
        #     print(f"Failed to download logo from {logo_url}")
        #     continue
        logo_path_relative = logo_filename.replace("../static", "")

        new_services[service_id] = {
            "id": service_id,
            "single_service": single_service,
            "link": link,
            "external_link": ext_link,
            "title": title,
            "description": description,
            "logo": logo_path_relative,
            "category": {
                "id": CATEGORY_ID,
                "name": CATEGORY_NAME,
                "ids": [CATEGORY_ID]
            }
        }

if not len(new_services):
    print("No new service found")
    exit()
        
output_path = os.path.join(OUTPUT_DIR, f"{SERVICE_NAME}.json")
with open(output_path, "w") as outfile:
    json.dump(list(new_services.values()), outfile, indent=4)

print(f"Services Data saved to {output_path}")

###########################
###########################
# Fetching details
###########################
###########################

NEW_SERVICES_FILE = output_path
OUT_DETAIL_FILE = f"./details/{SERVICE_NAME}.json"

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

def scrape_data(external_link, single_service, service_id, category_id):
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
    static_image_path = f"../static/images/{single_service}/{category_id}/{service_id}"
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
        single_service = item["single_service"]
        
        print(f"Processing service: {service_id}")
        scraped_data = scrape_data(external_link, single_service, service_id, category_id)
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


services_from_file = process_json_file(NEW_SERVICES_FILE)

# Save all services to a single JSON file
Path(os.path.dirname(OUT_DETAIL_FILE)).mkdir(parents=True, exist_ok=True)
with open(OUT_DETAIL_FILE, 'w') as outfile:
    json.dump(services_from_file, outfile, indent=4)

print(f"Saved all services to {OUT_DETAIL_FILE}")