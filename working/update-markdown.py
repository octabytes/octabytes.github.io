import os
import yaml
import re

# Directory containing markdown files
root_dir = "../content/fully-managed-open-source-services"

# Function to parse and transform markdown files
def process_markdown_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Split YAML and markdown content
    match = re.match(r"(?s)---\n(.*?)\n---\n(.*)", content)
    if not match:
        print(f"Skipping invalid file: {file_path}")
        return

    yaml_content = match.group(1)
    markdown_content = match.group(2)

    # Parse YAML content
    yaml_data = yaml.safe_load(yaml_content)

    # Extract and remove `content.description` and `content.features`
    content_data = yaml_data.get("content", {})
    description = content_data.pop("description", None)
    features = content_data.pop("features", [])

    # Update YAML content without description and features
    updated_yaml_content = yaml.dump(yaml_data, sort_keys=False)

    description_paragraphs = description.split("\n")
    formatted_description = "\n\n".join([f"{paragraph.strip()}" for paragraph in description_paragraphs])

    # Prepare markdown content
    description_md = f"## Overview\n\n{formatted_description}\n" if formatted_description else ""
    features_md = "## Features\n\n" + "\n\n".join(
        f"- ### {feature['title']}\n\n  {feature['description']}"
        for feature in features
    ) if features else ""

    new_markdown_content = f"---\n{updated_yaml_content}---\n\n{description_md}\n{features_md}"

    # Write back to the file
    with open(file_path, "w") as file:
        file.write(new_markdown_content)

# Walk through the directory and process markdown files
for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md") and not file.startswith("_index"):
            file_path = os.path.join(subdir, file)
            print(f"Processing file: {file_path}")
            process_markdown_file(file_path)
