import os
import yaml
import json

# Function to extract YAML content from a markdown file
def extract_yaml_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if '---' in lines[0]:  # Ensure the file starts with a YAML block
            yaml_start = lines.index('---\n')
            yaml_end = lines.index('---\n', yaml_start + 1)
            yaml_content = ''.join(lines[yaml_start + 1:yaml_end])
            return yaml.safe_load(yaml_content)
    return None

# Directory containing markdown files
content_dir = "../content"
output_file = "./descriptions.json"

# Collect data from markdown files
data = []

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith('.md') and file != "_index.md":
            filepath = os.path.join(root, file)
            yaml_data = extract_yaml_content(filepath)
            if yaml_data and 'content' in yaml_data and 'description' in yaml_data.get('meta', {}):
                entry = {
                    "id": yaml_data['content'].get('id', ''),
                    "description": yaml_data['meta']['description']
                }
                data.append(entry)

# Save collected data to a JSON file
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"Descriptions have been saved to {output_file}")
