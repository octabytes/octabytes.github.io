import os
import yaml

# Directory containing markdown files
root_dir = "../content/fully-managed-open-source-services"

# Function to process and update markdown files
def update_meta_cover(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md") and file != "_index.md":
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Split YAML front matter and markdown content
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) > 2:
                        yaml_content = parts[1]
                        markdown_content = parts[2]

                        try:
                            # Parse YAML content
                            data = yaml.safe_load(yaml_content)

                            # Update meta.cover with the first screenshot if available
                            if (
                                "meta" in data 
                                and "cover" in data["meta"]
                                and "content" in data
                                and "screenshots" in data["content"]
                                and len(data["content"]["screenshots"]) > 0
                            ):
                                first_screenshot = data["content"]["screenshots"][0]
                                data["meta"]["cover"] = first_screenshot

                                # Convert back to YAML
                                new_yaml_content = yaml.dump(data, sort_keys=False)

                                # Write updated content back to file
                                with open(file_path, "w", encoding="utf-8") as f:
                                    f.write("---\n" + new_yaml_content + "---" + markdown_content)

                                print(f"Updated: {file_path}")

                        except yaml.YAMLError as e:
                            print(f"Error parsing YAML in file {file_path}: {e}")

# Run the function
update_meta_cover(root_dir)
