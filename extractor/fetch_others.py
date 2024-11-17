import os
import json
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
        logo_response = requests.get(logo_url, stream=True)
        if logo_response.status_code == 200:
            with open(logo_filename, "wb") as img_file:
                img_file.write(logo_response.content)
            logo_path_relative = logo_filename.replace("../static", "")
        else:
            print(f"Failed to download logo from {logo_url}")
            continue

        new_services[service_id] = {
            "id": service_id,
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

        
output_path = os.path.join(OUTPUT_DIR, f"{SERVICE_NAME}.json")
with open(output_path, "w") as outfile:
    json.dump(list(new_services.values()), outfile, indent=4)

print(f"Services Data saved to {output_path}")