import csv
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

    print("->> checking", external_link)

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
        elif img_url.startswith('/'):
            img_url = '	https://elest.io' + img_url
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
            "single_service": single_service,
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

###################################
###################################
# Details into MarkDown
###################################
###################################

INPUT_DETAIL_FILE = f"./details/{SERVICE_NAME}.json"

# Load JSON data
with open(INPUT_DETAIL_FILE, 'r', encoding='utf-8') as f:
    services_detail = json.load(f)

# Helper function to properly escape YAML strings
def yaml_escape(text):
    line_text = " ".join(text.splitlines()).strip()
    line_text = line_text.replace('"', "'")

    return f'"{line_text}"' if ':' in line_text or "'" in line_text else line_text

# Process each entry and save as Markdown
for service in services_detail:
    category_id = service['category']['id']
    service_id = service['id']
    single_service = service.get('single_service', "")
    title = yaml_escape(service['title'])
    logo = service['logo']
    website = service['website']
    dashboard_image = service['screenshots'][0] if service['screenshots'] else ""
    long_description = yaml_escape(service['long_description'])
    short_description = yaml_escape(service['description'])
    features = service['features']
    screenshots = service['screenshots']

    if not single_service:
        if "applications/" in logo:
            single_service = "applications"
        elif "databases/" in logo:
            single_service = "databases"
        elif "development/" in logo:
            single_service = "development"
        elif "hosting-and-infrastructure/" in logo:
            single_service = "hosting-and-infrastructure"

    output_dir = f"../content/{single_service}/"

    # Create directory for category if it doesn't exist
    output_path = os.path.join(output_dir, category_id)
    os.makedirs(output_path, exist_ok=True)

    # Format Markdown content
    md_content = f"""---
draft: false
title: {title}
content:
  id: {service_id}
  name: {title}
  logo: {logo}
  website: {website}
  iframe_website: /website/{single_service}/{category_id}/{service_id}
  dashboardImage: {dashboard_image}
  short_description: {short_description}
  description: {long_description}
  features:
"""

    # Add features to markdown content
    for feature in features:
        feature_title = yaml_escape(feature['title'])
        feature_description = yaml_escape(feature['description'])
        md_content += f"    - title: {feature_title}\n      description: {feature_description}\n"

    # Add screenshots
    md_content += "  screenshots:\n"
    for screenshot in screenshots:
        md_content += f"    - {screenshot}\n"

    md_content += "---"

    # Write to markdown file
    output_file = os.path.join(output_path, f"{service_id}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"Markdown file created: {output_file}")

#########################################
#########################################
# Create website iframe
#########################################
#########################################

INPUT_FILE = f"./details/{SERVICE_NAME}.json"

# Load JSON data
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    services_detail = json.load(f)

# Helper function to properly escape YAML strings
def yaml_escape(text):
    line_text = " ".join(text.splitlines()).strip()
    line_text = line_text.replace('"', "'")

    return f'"{line_text}"' if ':' in line_text or "'" in line_text else line_text

# Process each entry and save as Markdown
for db in services_detail:
    category_id = db['category']['id']
    db_id = db['id']
    title = yaml_escape(db['title'])
    website = db['website']
    short_description = yaml_escape(db['description'])
    logo = db["logo"]
    single_service = db.get("single_service", "")

    if not single_service:
        if "applications/" in logo:
            single_service = "applications"
        elif "databases/" in logo:
            single_service = "databases"
        elif "development/" in logo:
            single_service = "development"
        elif "hosting-and-infrastructure/" in logo:
            single_service = "hosting-and-infrastructure"

    output_dir = f"../content/website/{single_service}/"

    # Create directory for category if it doesn't exist
    output_path = os.path.join(output_dir, category_id)
    os.makedirs(output_path, exist_ok=True)

    # Format Markdown content
    md_content = f"""---
draft: false
title: {title}
content:
  id: {db_id}
  name: {title}
  website: {website}
  short_description: {short_description}
"""

    md_content += "---"

    # Write to markdown file
    output_file = os.path.join(output_path, f"{db_id}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"Iframe Markdown file created: {output_file}")


#########################################
#########################################
# Create Nginx Files
#########################################
#########################################


# Define input and output folders
INPUT_FILE = f"./details/{SERVICE_NAME}.json"
OUT_FOLDER = f"./nginx"

# Ensure the output folder exists
os.makedirs(OUT_FOLDER, exist_ok=True)

# Template for the NGINX configuration file (use double curly braces for literal curly braces)
nginx_template = """server {{
    listen 80;
    server_name {id}.reverse-proxy.octabyte.io;

    location / {{
        proxy_pass {website};
        proxy_set_header Host $proxy_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Optional: Remove the X-Frame-Options header to allow iframing
        proxy_hide_header X-Frame-Options;
        proxy_hide_header Content-Security-Policy;

        # Timeout settings (optional)
        proxy_connect_timeout 5s;
        proxy_read_timeout 300s;
        proxy_send_timeout 300s;
    }}
}}
"""

# Function to process each JSON file
def process_json_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            for entry in data:
                # Extract id and website
                service_id = entry.get('id')
                website = entry.get('website')

                # Skip if either id or website is missing
                if not service_id or not website:
                    print(f"Skipping entry in {file_path} due to missing id or website.")
                    continue

                # Create NGINX config content
                nginx_conf = nginx_template.format(id=service_id, website=website)

                # Define output file path
                output_file_path = os.path.join(OUT_FOLDER, f"{service_id}.conf")

                # Write the configuration to a file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(nginx_conf)

                print(f"Created NGINX config for {service_id} at {output_file_path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in {file_path}: {e}")


print(f"Processing {INPUT_FILE}...")
process_json_file(INPUT_FILE)

print("NGINX configuration generation completed.")

############################################
############################################
# Auto Posting
############################################
############################################

INPUT_FILE = f"./details/{SERVICE_NAME}.json"
OUT_FOLDER = "./auto_posting"
IMAGE_PREFIX = '/Users/haider/codeplace/octabyte/octabytes.github.io/static'

# Ensure the output folder exists
os.makedirs(OUT_FOLDER, exist_ok=True)

def generate_category_hashtags(category_ids):
    hashtags = []
    for cat_id in category_ids:
        if "-" in cat_id:
            # Remove hyphens and create a combined hashtag
            combined_tag = f"#{cat_id.replace('-', '')}"
            hashtags.append(combined_tag)
            
            # Create individual word hashtags
            words = cat_id.split('-')
            word_tags = [f"#{word}" for word in words]
            hashtags.extend(word_tags)
        else:
            hashtags.append(f"#{cat_id}")
    
    return " ".join(hashtags)

def generate_filename_hashtag(filename):
    if filename == "hosting-and-infrastructure":
        # Special case: Use separate hashtags
        return "#hosting #infrastructure"
    else:
        # General case: Remove hyphens and merge the words
        return f"#{filename.replace('-', '')}"

def create_csv_data(data):
    title = data.get("title", "")
    description = data.get("description", "")
    long_description = data.get("long_description", "")
    features = data.get("features", [])
    dashboard_image = f"{IMAGE_PREFIX}{data.get('dashboardImage', '')}"
    logo = data["logo"]
    single_service = data.get("single_service", None)

    if not single_service:
        if "applications/" in logo:
            single_service = "applications"
        elif "databases/" in logo:
            single_service = "databases"
        elif "development/" in logo:
            single_service = "development"
        elif "hosting-and-infrastructure/" in logo:
            single_service = "hosting-and-infrastructure"

    website_link = f"https://octabyte.io/{single_service}/{data['category']['id']}/{data['id']}"

    # Generate feature highlights with the new format
    feature_highlights = "\n\n".join(
        [f"- {feature['title']}:\n\n{feature['description']}" for feature in features]
    )
    
    # Generate hashtags
    category_hashtags = generate_category_hashtags(data["category"]["ids"])
    filename_hashtag = generate_filename_hashtag(single_service)
    id_hashtag = f"#{data['id'].replace('-', '')}"
    hashtags = f"#octabyte #opensource #devops #itservices {filename_hashtag} {category_hashtags} {id_hashtag} #managedservices"
    
    # Create post content
    post_content = (
        f"{title}\n\n"
        f"{long_description}\n\n"
        f"Features Highlight:\n\n"
        f"{feature_highlights}\n\n"
        f"{website_link}\n\n"
        f"{hashtags}"
    )

    dashboard_image = dashboard_image.strip()
    
    # Return CSV row data
    return [
        post_content,
        dashboard_image,
        website_link,
        hashtags,
        feature_highlights,
        description,
        title
    ]

csv_file_path = os.path.join(OUT_FOLDER, f"{SERVICE_NAME}.csv")

with open(INPUT_FILE, 'r') as file:
    data = json.load(file)
    csv_data = []

    for software in data:
        csv_row = create_csv_data(software)
        csv_data.append(csv_row)

    # Write data to CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow([
            "Post Content",
            "Dashboard Image URL",
            "Website Link",
            "Hashtags",
            "Features Highlights",
            "Description",
            "Title"
        ])
        # Write rows
        writer.writerows(csv_data)

print(f"AUto posting CSV file created: {csv_file_path}")

#######################################
#######################################
# Create services page
#######################################
#######################################

services_file = f"./services/{SERVICE_NAME}.json"

with open(services_file, "r") as f:
    services = json.load(f)

def json_to_markdown(services):
    md_content = """---
"""

    md_content += "  services:\n"

    # Add service information
    for service in services:
        category_ids = " ".join(service["category"]["ids"])
        
        # Wrap description in quotes if it contains a colon
        description = service['description']
        if ':' in description:
            description = f'"{description}"'
        
        md_content += f"    - id: {service['id']}\n"
        md_content += f"      title: {service['title']}\n"
        md_content += f"      image: {service['logo']}\n"
        md_content += f"      url: {service['link']}\n"
        md_content += f"      category: {category_ids}\n"
        md_content += f"      description: {description}\n"

    md_content += "---"
    return md_content

# Generate markdown content
markdown_content = json_to_markdown(services)

output_md_file = "./services_list/list.md"

os.makedirs("./services_list", exist_ok=True)

# Write to markdown file
with open(output_md_file, "w") as f:
    f.write(markdown_content)

print(f"Service list Markdown file generated at {output_md_file}")
