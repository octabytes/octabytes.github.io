import json

# File paths
categories_file = "./categories/databases.json"
services_file = "./services/databases.json"
output_md_file = "./output/databases.md"

# Load JSON data
with open(categories_file, "r") as f:
    categories = json.load(f)

with open(services_file, "r") as f:
    services = json.load(f)

# Convert category and service data into Markdown format
def json_to_markdown(categories, services):
    md_content = """---
title: "Databases"
draft: false
layout: "services"

content:
  id: "databases"
  title: "'Databases'"
  description: REPLACE_THIS
  categories:
"""

    # Add category information
    for category in categories:
        md_content += f"    - id: {category['id']}\n"
        md_content += f"      name: {category['name']}\n"

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
markdown_content = json_to_markdown(categories, services)

# Write to markdown file
with open(output_md_file, "w") as f:
    f.write(markdown_content)

print(f"Markdown file generated at {output_md_file}")
