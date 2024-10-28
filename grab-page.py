import os
import requests
import yaml
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path

# Define paths
DATA_FILE = "./data/databases.yaml"
BASE_IMAGE_PATH = "./static/images/databases/"
BASE_MD_PATH = "./content/databases/"

# Load YAML data
with open(DATA_FILE, 'r') as file:
    data = yaml.safe_load(file)

def fetch_page_content(url):
    """Fetch HTML content of a page."""
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def download_image(img_url, save_path, page_url):
    """Download and save image from a given URL, joining with page URL if relative."""
    img_url = urljoin(page_url, img_url)  # Join relative paths with page URL
    img_url = "https:" + img_url if img_url.startswith("//") else img_url
    response = requests.get(img_url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)

def get_content(soup, selector, attr=None):
    """Extract text or attribute content from the first element that matches the selector."""
    element = soup.select_one(selector)
    if element:
        return element.get(attr) if attr else element.text.strip()
    return None

def get_screenshots(soup, img_folder_path, page_url):
    """Fetch and save only the first two screenshots from the HTML."""
    screenshot_paths = []
    screenshots = soup.select('.product__screenshots img')
    for idx, img in enumerate(screenshots[:2], start=1):  # Only take first two images
        img_url = img.get("src")
        img_ext = img_url.split('.')[-1]
        img_name = "dashboard." + img_ext if idx == 1 else f"screenshot-2.{img_ext}"
        save_path = os.path.join(img_folder_path, img_name)
        download_image(img_url, save_path, page_url)
        screenshot_paths.append(save_path.replace('./static', ''))  # Remove './static' from path
    return screenshot_paths

def get_features(soup):
    """Extract features titles and descriptions from the HTML."""
    features = []
    features_div = soup.select('.benefits__cards--features .benefits__informations')
    for feature in features_div:
        title = get_content(feature, '.benefits__header p.benefits__title')
        description = get_content(feature, 'p:not(.benefits__title)')
        if title and description:
            features.append({"title": title, "description": description})
    return features

def yaml_safe_text(text):
    """Wrap text in double quotes if it contains a colon to prevent YAML errors."""
    return f'"{text}"' if ':' in text else text

def generate_md_file(content, save_path):
    """Generate the markdown file from content."""
    with open(save_path, 'w') as md_file:
        md_file.write("---\n")
        md_file.write(f"draft: false\n")
        md_file.write(f"title: {content['title']}\n")
        md_file.write("content:\n")
        md_file.write(f"  name: {content['name']}\n")
        md_file.write(f"  logo: {content['logo']}\n")
        md_file.write(f"  videoUrl: REPLACE\n")
        md_file.write(f"  website: {content['website']}\n")
        md_file.write(f"  dashboardImage: {content['dashboardImage']}\n")
        md_file.write(f"  description: {yaml_safe_text(content['description'])}\n")
        md_file.write("  features:\n")
        for feature in content['features']:
            md_file.write(f"    - title: {yaml_safe_text(feature['title'])}\n")
            md_file.write(f"      description: {yaml_safe_text(feature['description'])}\n")
        md_file.write("  screenshots:\n")
        for screenshot in content['screenshots']:
            md_file.write(f"    - {screenshot}\n")
        md_file.write("---\n")

# Process each service in YAML data
for service in data['services']:
    title = service['title']
    category = service['category']
    external_link = service['external_link']
    logo_path = service['image']  # Use logo path as it is
    url = service['url']
    lowercase_title = title.lower()

    print(f"Processing {title}...")

    # Create directories for images and markdown
    img_folder_path = os.path.join(BASE_IMAGE_PATH, category, lowercase_title)
    md_file_path = os.path.join(BASE_MD_PATH, category, f"{lowercase_title}.md")
    Path(img_folder_path).mkdir(parents=True, exist_ok=True)
    Path(os.path.dirname(md_file_path)).mkdir(parents=True, exist_ok=True)

    try:
        # Fetch page content
        soup = fetch_page_content(external_link)

        # Extract data
        website = get_content(soup, '.benefits__main--description a', 'href')
        description = get_content(soup, '.about-header p.about-description')
        screenshots = get_screenshots(soup, img_folder_path, external_link)
        features = get_features(soup)

        # Prepare content for markdown file
        content = {
            "title": title,
            "name": title,
            "logo": logo_path,  # Use the logo path as it is
            "website": website,
            "dashboardImage": screenshots[0] if screenshots else "",
            "description": description,
            "features": features,
            "screenshots": screenshots,
        }

        # Generate markdown file
        generate_md_file(content, md_file_path)
        print(f"Finished processing {title}.")
    except Exception as e:
        print(f"Error processing {title}: {e}")
