import yaml
import json
import os

# Load YAML file
input_file = "../data/services.yaml"
output_folder = "./services"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read YAML file
with open(input_file, 'r') as file:
    data = yaml.safe_load(file)

# Process each top-level item in catalog_list
for catalog in data.get("catalog_list", []):
    file_name = f"{catalog['id']}.json"  # Use `id` field as file name
    file_path = os.path.join(output_folder, file_name)
    
    # Save the services for this catalog as JSON
    with open(file_path, 'w') as json_file:
        json.dump(catalog, json_file, indent=4)

print("Conversion completed. JSON files saved in ./services")
