import os
import json

# Define input and output folders
input_folder = './details'
output_folder = './nginx'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Template for the NGINX configuration file (use double curly braces for literal curly braces)
nginx_template = """server {{
    listen 80;
    server_name {id}.reverse-proxy.octabyte.io;

    location / {{
        proxy_pass {website};
        proxy_set_header Host $proxy_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Optional: Remove the X-Frame-Options header to allow iframing
        proxy_hide_header X-Frame-Options;
        proxy_hide_header Content-Security-Policy;

        # Timeout settings (optional)
        proxy_connect_timeout 5s;
        proxy_read_timeout 300s;
        proxy_send_timeout 300s;
    }}
}}
"""

# Function to process each JSON file
def process_json_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            for entry in data:
                # Extract id and website
                service_id = entry.get('id')
                website = entry.get('website')

                # Skip if either id or website is missing
                if not service_id or not website:
                    print(f"Skipping entry in {file_path} due to missing id or website.")
                    continue

                # Create NGINX config content
                nginx_conf = nginx_template.format(id=service_id, website=website)

                # Define output file path
                output_file_path = os.path.join(output_folder, f"{service_id}.conf")

                # Write the configuration to a file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(nginx_conf)

                print(f"Created NGINX config for {service_id} at {output_file_path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in {file_path}: {e}")

# Iterate over all JSON files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(input_folder, filename)
        print(f"Processing {file_path}...")
        process_json_file(file_path)

print("NGINX configuration generation completed.")
