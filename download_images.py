import os
import re
import requests
from pathlib import Path
import hashlib
import yaml

# Root folder where your markdown files are located
content_root = "content"

# Destination folder to save images
static_image_root = "static/images"

# Regex pattern to find image URLs (without capturing groups to avoid tuple return)
image_url_pattern = re.compile(r"(https://cf\.appdrag\.com[^\s]+\.(png|jpg))")

def generate_unique_name(url, prefix, extension):
    """Generate a unique file name using a hash of the URL."""
    url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
    return f"{prefix}.{extension}"

def download_image(url, save_path):
    """Download the image from a URL and save it to the given path."""
    response = requests.get(url)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {save_path}")

def process_markdown_file(file_path):
    """Process a markdown file, download images, and update the URLs."""
    with open(file_path, "r") as file:
        content = file.read()

    # Split the YAML front matter from the rest of the file
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"Skipping {file_path}, no valid front matter.")
        return

    # Parse the YAML part
    try:
        front_matter = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {file_path}: {e}")
        return

    # Check if 'content' key exists
    if 'content' not in front_matter:
        print(f"Skipping {file_path}, 'content' key missing in front matter.")
        return

    # Extract the URLs from specific fields (logo, dashboardImage, screenshots)
    images_to_download = []

    content = front_matter['content']
    if 'logo' in content:
        images_to_download.append(('logo', content['logo']))
    if 'dashboardImage' in content:
        images_to_download.append(('dashboard', content['dashboardImage']))
    if 'screenshots' in content:
        for i, screenshot in enumerate(content['screenshots'], 1):
            images_to_download.append((f'screenshot-{i}', screenshot))

    # Build the destination folder path based on the markdown file's relative path
    relative_folder = file_path.replace(content_root, "").replace(".md", "").lower().strip("/")
    save_folder = os.path.join(static_image_root, relative_folder)

    # Process each image link and update the front matter with the new local path
    for image_type, url in images_to_download:
        image_extension = url.split(".")[-1]
        unique_image_name = generate_unique_name(url, image_type, image_extension)
        save_path = os.path.join(save_folder, unique_image_name)
        download_image(url, save_path)

        # Replace the URL in the front matter with the new local path
        if image_type.startswith('logo'):
            front_matter['content']['logo'] = f"/images/{relative_folder}/{unique_image_name}"
        elif image_type.startswith('dashboard'):
            front_matter['content']['dashboardImage'] = f"/images/{relative_folder}/{unique_image_name}"
        elif image_type.startswith('screenshot'):
            screenshot_index = int(image_type.split('-')[1]) - 1
            front_matter['content']['screenshots'][screenshot_index] = f"/images/{relative_folder}/{unique_image_name}"

    # Rebuild the updated content with the modified front matter
    updated_content = f"---\n{yaml.dump(front_matter)}---\n{parts[2]}"

    # Write the updated content back to the file
    with open(file_path, "w") as file:
        file.write(updated_content)

def process_all_markdown_files():
    """Go through all markdown files in the content directory and process them."""
    for root, dirs, files in os.walk(content_root):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_markdown_file(file_path)

if __name__ == "__main__":
    process_all_markdown_files()
