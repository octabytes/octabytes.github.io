import os
import re

# Input and output directories
input_dir = "./nginx"
output_dir = "./nginx-converted"

# SSL settings to insert
ssl_config = """
    ssl_certificate /etc/nginx/ssl/cloudflare.pem;
    ssl_certificate_key /etc/nginx/ssl/cloudflare.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
"""

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

def extract_service_id(server_name):
    """Extract the service ID from the server_name."""
    return server_name.split('.')[0]

def convert_nginx_conf(file_path):
    """Convert NGINX configuration to the new format."""
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract the server_name
    match = re.search(r"server_name\s+([\w.-]+);", content)
    if not match:
        return None

    old_server_name = match.group(1)
    service_id = extract_service_id(old_server_name)
    new_server_name = f"{service_id}.inbzar.com"

    # Replace server_name and update listen directive
    content = re.sub(r"server_name\s+[\w.-]+;", f"server_name {new_server_name};", content)
    content = content.replace("listen 80;", "listen 443 ssl;")
    
    # Insert SSL configuration
    content = content.replace("server_name", ssl_config + "\n    server_name")

    # Create the HTTP-to-HTTPS redirect block
    redirect_block = f"""
server {{
    listen 80;
    server_name {new_server_name};
    return 301 https://$host$request_uri;
}}
"""

    # Append the redirect block to the configuration
    content += redirect_block
    return content

# Process each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".conf"):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)
        
        new_content = convert_nginx_conf(input_file_path)
        if new_content:
            with open(output_file_path, 'w') as f:
                f.write(new_content)

print("Conversion complete.")
