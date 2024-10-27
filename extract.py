import os
import requests
from bs4 import BeautifulSoup
import yaml

# Path to the HTML file
html_file_path = "tmp.html"

# Define output paths
images_base_path = "./static/images/development/no-code"
yaml_path = "./data/development.yaml"

# Load HTML content from the file
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
cards = soup.find_all("a", class_="card-container")

# Prepare the YAML structure
development_data = {"content": {"services": []}}

# Process each card
for card in cards:
    # Extracting item name, description, link, and image URL
    link = card['href']
    item_name = card.select_one(".template__label").get_text().strip().lower()
    title = item_name.capitalize()
    description = card.select_one(".template__description").get_text().strip()
    description = " ".join(description.split())  # Remove extra whitespace and line breaks
    image_url = card.select_one("img")["src"]

    # Construct URLs
    new_link = f"/development/no-code/{item_name}"
    external_link = f"https://elest.io{link}"

    # Download and save the image
    image_save_path = os.path.join(images_base_path, item_name, "logo.png")
    os.makedirs(os.path.dirname(image_save_path), exist_ok=True)
    image_data = requests.get(image_url).content
    with open(image_save_path, "wb") as image_file:
        image_file.write(image_data)

    # Append to development data
    development_data["content"]["services"].append({
        "category": "no-code",
        "description": description,
        "image": f"/images/development/no-code/{item_name}/logo.png",
        "title": title,
        "url": new_link,
        "external_link": external_link
    })

# Save the YAML file
os.makedirs(os.path.dirname(yaml_path), exist_ok=True)
with open(yaml_path, "w") as yaml_file:
    yaml.dump(development_data, yaml_file, default_flow_style=False)

print("Data extraction and file creation completed successfully.")
