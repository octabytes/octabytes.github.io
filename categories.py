import requests
from bs4 import BeautifulSoup
import json
import os

def extract_categories(service_name):
    # Define the URL and the headers to mimic a browser request
    url = f"https://elest.io/fully-managed-services/{service_name}"
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
            href = a_tag["href"]
            link = href.replace("/fully-managed-services", "")
            external_link = link if link.startswith("https://") else f"https://elest.io{href}"
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
        os.makedirs("./extractor/categories", exist_ok=True)

        # Save the extracted data to a JSON file
        file_path = f"./extractor/categories/{service_name}.json"
        with open(file_path, "w") as f:
            json.dump(categories, f, indent=4)
            print(f"Saved data to ./extractor/categories/{service_name}.json")
    else:
        print("Failed to fetch the page. Status code:", response.status_code)

names = ["databases", "applications", "development", "hosting-and-infrastructure"]

for name in names:
    extract_categories(name)