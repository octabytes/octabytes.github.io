import os
import json

# Load JSON data
input_file = './details/hosting-and-infrastructure.json'
output_dir = '../content/hosting-and-infrastructure/'

# Load JSON data
with open(input_file, 'r', encoding='utf-8') as f:
    hosting_and_infrastructure = json.load(f)

# Helper function to wrap text with double quotes if it contains a colon
def wrap_if_colon(text):
    return f'"{text}"' if ':' in text else text

# Process each entry and save as Markdown
for db in hosting_and_infrastructure:
    category_id = db['category']['id']
    db_id = db['id']
    title = db['title']
    logo = db['logo']
    website = db['website']
    dashboard_image = db['screenshots'][0] if db['screenshots'] else ""
    long_description = wrap_if_colon(db['long_description'])
    short_description = wrap_if_colon(db['description'])
    features = db['features']
    screenshots = db['screenshots']

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
  logo: {logo}
  website: {website}
  iframe_website: /website-iframe/hosting-and-infrastructure/{category_id}/{db_id}
  dashboardImage: {dashboard_image}
  short_description: {short_description}
  description: {long_description}
  features:
"""

    # Add features to markdown content
    for feature in features:
        feature_title = feature['title']
        feature_description = wrap_if_colon(feature['description'])
        md_content += f"    - title: {feature_title}\n      description: {feature_description}\n"

    # Add screenshots
    md_content += "  screenshots:\n"
    for screenshot in screenshots:
        md_content += f"    - {screenshot}\n"

    md_content += "---"

    # Write to markdown file
    output_file = os.path.join(output_path, f"{db_id}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"Markdown file created: {output_file}")
