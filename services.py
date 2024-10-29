import os
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urljoin, urlparse

# Paths
json_input_path = "./extractor/categories/development.json"
output_dir = "./extractor/development"
images_dir = "./static/images/development"

# Ensure directories exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(images_dir, exist_ok=True)

# Load category data
with open(json_input_path, "r") as file:
    categories = json.load(file)

# Process each category
for category in tqdm(categories, desc="Processing categories"):
    category_id = category["id"]
    category_name = category["name"]
    external_link = category["external_link"]

    # Fetch the external page with explicit encoding
    response = requests.get(external_link)
    response.encoding = 'utf-8'  # Set encoding if necessary
    if response.status_code != 200:
        print(f"Failed to fetch {external_link}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # Attempt to locate #cards container
    cards_container = soup.select_one("#cards") or soup.find("div", id="cards")
    if not cards_container:
        print(f"No #cards container found for {external_link}")
        continue

    links_data = []
    for a_tag in cards_container.find_all("a", href=True, class_="card-container"):
        href = a_tag["href"].strip("/")
        link = f"/development/{category_id}/{href.split('/')[-1]}"
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
        logo_path = f"{images_dir}/{category_id}/{href.split('/')[-1]}"
        os.makedirs(logo_path, exist_ok=True)
        logo_filename = f"{logo_path}/logo{logo_ext}"

        # Download the logo image
        logo_response = requests.get(logo_url, stream=True)
        if logo_response.status_code == 200:
            with open(logo_filename, "wb") as img_file:
                img_file.write(logo_response.content)
            logo_path_relative = logo_filename.replace("./static", "")
        else:
            print(f"Failed to download logo from {logo_url}")
            continue

        # Add link data
        links_data.append({
            "category": {
                "id": category_id,
                "name": category_name
            },
            "link": link,
            "external_link": ext_link,
            "title": title,
            "description": description,
            "logo": logo_path_relative
        })

    # Save data for this category
    output_path = os.path.join(output_dir, f"{category_id}.json")
    with open(output_path, "w") as outfile:
        json.dump(links_data, outfile, indent=4)
    print(f"Data saved to {output_path}")
