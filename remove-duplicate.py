import os
import json

def extract_data_from_json_files(input_directory, output_file):
    all_data = []
    category_ids = {}

    # Get a list of all JSON files in the input directory
    json_files = [f for f in os.listdir(input_directory) if f.endswith('.json')]
    total_files = len(json_files)

    for index, json_file in enumerate(json_files):
        file_path = os.path.join(input_directory, json_file)
        
        # Read the JSON file
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file: {file_path}")
                continue

            # Process each item in the JSON data
            for item in data:
                item_id = item['link'].split('/')[-1]  # Extract id from link
                item['id'] = item_id  # Add id field to item
                
                # Add category ids
                category_id = item['category']['id']
                if category_id not in category_ids:
                    category_ids[category_id] = {'ids': [category_id]}
                
                # Check for duplicates before adding the id
                if item_id not in category_ids[category_id]['ids']:
                    category_ids[category_id]['ids'].append(item_id)

                all_data.append(item)

        # Show progress
        print(f"Processed file {index + 1}/{total_files}: {json_file}")

    # Combine category data with all data
    for item in all_data:
        category_id = item['category']['id']
        if category_id in category_ids:
            item['category']['ids'] = category_ids[category_id]['ids']

    # Write the aggregated data to the output file
    with open(output_file, 'w') as outfile:
        json.dump(all_data, outfile, indent=4)

    print(f"Data extraction complete. Output saved to: {output_file}")

# Specify input and output directories
input_directory = './extractor/databases'
output_file = './extractor/services/databases.json'

# Run the data extraction
extract_data_from_json_files(input_directory, output_file)
