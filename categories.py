import requests
from bs4 import BeautifulSoup
import json
import os

# 1. databases
# 2. applications
# 3. development
# 4. hosting-and-infrastructure

# Define the URL and the headers to mimic a browser request
url = "https://elest.io/fully-managed-services/hosting-and-infrastructure"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

# Fetch the HTML content
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Fetched the page successfully.")
    soup = BeautifulSoup(response.content, "html.parser")

    # Locate the category container
    category_container = soup.select_one("body > section.services.category.visible > div > div.tabs__subCategories")
    
    # Initialize the list to hold category data
    categories = []

    # Loop through each 'a' tag within the container
    for a_tag in category_container.find_all("a", href=True):
        link = a_tag["href"].replace("/fully-managed-services", "")
        external_link = link if link.startswith("https://") else f"https://elest.io{link}"
        id = link.split("/")[-1]
        name = a_tag.get_text(strip=True)

        # Append category data to the list
        categories.append({
            "link": link,
            "external_link": external_link,
            "id": id,
            "name": name
        })

        # Print progress
        print(f"Processed category: {name}")

    # Create the directory if it doesn't exist
    os.makedirs("./categories", exist_ok=True)

    # Save the extracted data to a JSON file
    with open("./categories/hosting-and-infrastructure.json", "w") as f:
        json.dump(categories, f, indent=4)
        print("Saved data to ./categories/hosting-and-infrastructure.json")
else:
    print("Failed to fetch the page. Status code:", response.status_code)
