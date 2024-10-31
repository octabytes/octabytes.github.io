import os
import json

# Load JSON data
input_file = './details/hosting-and-infrastructure.json'
output_dir = '../content/website-iframe/hosting-and-infrastructure/'

# Load JSON data
with open(input_file, 'r', encoding='utf-8') as f:
    hosting_and_infrastructure = json.load(f)

# Helper function to properly escape YAML strings
def yaml_escape(text):
    line_text = " ".join(text.splitlines()).strip()
    line_text = line_text.replace('"', "'")

    return f'"{line_text}"' if ':' in line_text or "'" in line_text else line_text
    
# Process each entry and save as Markdown
for db in hosting_and_infrastructure:
    category_id = db['category']['id']
    db_id = db['id']
    title = yaml_escape(db['title'])
    website = db['website']
    short_description = yaml_escape(db['description'])

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

    print(f"Markdown file created: {output_file}")
