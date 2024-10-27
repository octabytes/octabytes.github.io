import yaml

# Load YAML file
file_path = "./data/tmp.yaml"
with open(file_path, "r") as file:
    data = yaml.safe_load(file)

# Process 'databases' section
titles_seen = {}
unique_databases = []

for db in data["content"]["databases"]:
    title = db["title"]
    if title in titles_seen:
        # If title already seen, append the category to the first entry with this title
        titles_seen[title]["category"] += " " + db["category"]
    else:
        # If title is new, add it to the list and store reference
        titles_seen[title] = db
        unique_databases.append(db)

# Update data with unique entries
data["content"]["databases"] = unique_databases

# Save updated YAML file
with open(file_path, "w") as file:
    yaml.dump(data, file)

print("Duplicates processed, YAML file updated.")
