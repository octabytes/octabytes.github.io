import os
import json
import re

# Paths
markdown_dir = "../content/website"
description_file = "./descriptions.json"

# Load descriptions from JSON
def load_descriptions(json_path):
    with open(json_path, "r") as f:
        return {item["id"]: item for item in json.load(f)}

# Update a markdown file
def update_markdown_file(file_path, descriptions):
    with open(file_path, "r") as f:
        content = f.read()

    # Extract the `id` from the markdown file
    match = re.search(r"id:\s*(\w+)", content)
    if not match:
        return False  # Skip if no id found

    item_id = match.group(1)
    if item_id not in descriptions:
        return False  # Skip if id not in descriptions.json

    # Get the new title and description
    new_title = f"{descriptions[item_id]['name']} - {descriptions[item_id]['title']}"
    new_description = descriptions[item_id]['description']

    # Update the content
    content = re.sub(r"title:.*", f"title: \"{new_title}\"", content)
    content = re.sub(r"description:.*", f"description: \"{new_description}\"", content)

    # Write the updated content back to the file
    with open(file_path, "w") as f:
        f.write(content)

    return True

# Main function
def main():
    descriptions = load_descriptions(description_file)

    # Walk through the markdown directory
    for root, _, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                updated = update_markdown_file(file_path, descriptions)
                if updated:
                    print(f"Updated: {file_path}")
                else:
                    print(f"Skipped: {file_path}")

if __name__ == "__main__":
    main()
