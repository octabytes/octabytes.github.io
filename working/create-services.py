import json

# Load JSON data from files
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def merge_and_create_markdown(databases_path, descriptions_path, output_md_path):
    # Load data from JSON files
    databases = load_json(databases_path)
    descriptions = load_json(descriptions_path)

    # Create a dictionary for descriptions keyed by 'id'
    descriptions_dict = {desc['id']: desc['description'] for desc in descriptions}

    # Build Markdown content
    markdown_lines = []

    markdown_lines.append("catalog_list:")
    markdown_lines.append(f"  - name: {databases['name']}")
    markdown_lines.append(f"    id: {databases['id']}")
    markdown_lines.append("    services:")

    for service in databases['services']:
        service_id = service['id']
        description = descriptions_dict.get(service_id, service['description'])
        
        markdown_lines.append("      - id: " + service_id)
        markdown_lines.append("        title: " + service['title'])
        markdown_lines.append("        image: " + service['image'])
        markdown_lines.append("        url: " + service['url'])
        markdown_lines.append("        category: " + service['category'])
        markdown_lines.append("        description: " + description)

    # Save Markdown content to file
    with open(output_md_path, 'w') as file:
        file.write("\n".join(markdown_lines))

# Paths to input and output files
databases_json_path = "./services/hosting-and-infrastructure.json"
descriptions_json_path = "./descriptions.json"
output_md_path = "./services.md"

# Execute the script
merge_and_create_markdown(databases_json_path, descriptions_json_path, output_md_path)
