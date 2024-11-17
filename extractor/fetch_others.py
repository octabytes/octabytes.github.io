import os
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urljoin, urlparse

def extract_services(service_name):
    # Paths
    json_input_path = f"./services/{service_name}.json"
    output_dir = f"./others"
    images_dir = f"../static/images/{service_name}"

    # Ensure directories exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)

    # Load category data
    with open(json_input_path, "r") as file:
        services = json.load(file)

    category_id = "others"

    service_data = {}

    external_link = f"https://elest.io/fully-managed-services/{service_name}"

    # Fetch the external page with explicit encoding
    response = requests.get(external_link)
    response.encoding = 'utf-8'  # Set encoding if necessary
    if response.status_code != 200:
        print(f"Failed to fetch {external_link}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Attempt to locate #cards container
    cards_container = soup.select_one("#cards") or soup.find("div", id="cards")
    if not cards_container:
        print(f"No #cards container found for {external_link}")
        return

    for a_tag in cards_container.find_all("a", href=True, class_="card-container"):
        href = a_tag["href"].strip("/")
        service_id = href.split('/')[-1]  # Create ID for the service item

        id_exist = any(obj['id'] == service_id for obj in services)

        if id_exist:
            continue

        link = f"/{service_name}/{category_id}/{service_id}"
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
        logo_path = f"{images_dir}/{category_id}/{service_id}"
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

        # Create service item if it does not exist
        if service_id not in service_data:
            service_data[service_id] = {
                "id": service_id,
                "link": link,
                "external_link": ext_link,
                "title": title,
                "description": description,
                "logo": logo_path_relative,
                "category": {
                    "id": category_id,
                    "name": "Others",
                    "ids": [category_id]  # Initialize ids with category_id
                }
            }
        else:
            # If service item exists, append category_id to ids
            if category_id not in service_data[service_id]["category"]["ids"]:
                service_data[service_id]["category"]["ids"].append(category_id)

        

    # Save all services in a single file
    output_path = os.path.join(output_dir, f"{service_name}.json")
    with open(output_path, "w") as outfile:
        json.dump(list(service_data.values()), outfile, indent=4)
    print(f"Data saved to {output_path}")

# names = ["databases", "applications", "development", "hosting-and-infrastructure"]
names = ["applications"]

for name in names:
    print("===============================================")
    print(f"              Extracting {name}               ")
    print("===============================================")

    extract_services(name)
