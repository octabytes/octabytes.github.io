import json
import os
import csv

# Input and output folders
DETAILS_FOLDER = './details'
CSV_OUTPUT_FOLDER = './csv_data'
IMAGE_PREFIX = '/Users/haider/codeplace/octabyte/octabytes.github.io'

# Ensure the output folder exists
os.makedirs(CSV_OUTPUT_FOLDER, exist_ok=True)

def generate_category_hashtags(category_ids):
    hashtags = []
    for cat_id in category_ids:
        # Remove hyphens and create a combined hashtag
        combined_tag = f"#{cat_id.replace('-', '')}"
        hashtags.append(combined_tag)
        
        # Create individual word hashtags
        words = cat_id.split('-')
        word_tags = [f"#{word}" for word in words]
        hashtags.extend(word_tags)
    
    return " ".join(hashtags)

def generate_filename_hashtag(filename):
    if filename == "hosting-and-infrastructure":
        # Special case: Use separate hashtags
        return "#hosting #infrastructure"
    else:
        # General case: Remove hyphens and merge the words
        return f"#{filename.replace('-', '')}"

def create_csv_data(data, filename):
    title = data.get("title", "")
    description = data.get("description", "")
    long_description = data.get("long_description", "")
    features = data.get("features", [])
    dashboard_image = f"{IMAGE_PREFIX}{data.get('dashboardImage', '')}"
    website_link = f"https://octabyte.io/{filename}/{data['category']['id']}/{data['id']}"

    # Generate feature highlights with the new format
    feature_highlights = "\n\n".join(
        [f"- {feature['title']}:\n\n{feature['description']}" for feature in features]
    )
    
    # Generate hashtags
    category_hashtags = generate_category_hashtags(data["category"]["ids"])
    filename_hashtag = generate_filename_hashtag(filename)
    id_hashtag = f"#{data['id'].replace('-', '')}"
    hashtags = f"#octabyte #opensource #devops #itservices {filename_hashtag} {category_hashtags} {id_hashtag} #managedservices"
    
    # Create post content
    post_content = (
        f"{title}\n\n"
        f"{long_description}\n\n"
        f"Features Highlight:\n\n"
        f"{feature_highlights}\n\n"
        f"{website_link}\n\n"
        f"{hashtags}"
    )
    
    # Return CSV row data
    return [
        post_content,
        dashboard_image,
        website_link,
        hashtags,
        feature_highlights,
        description,
        title
    ]

def process_json_files():
    # Iterate through all JSON files in the folder
    for filename in os.listdir(DETAILS_FOLDER):
        if filename.endswith(".json"):
            file_path = os.path.join(DETAILS_FOLDER, filename)
            csv_file_path = os.path.join(CSV_OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}.csv")
            filename_without_ext = os.path.splitext(filename)[0]

            with open(file_path, 'r') as file:
                data = json.load(file)
                csv_data = []

                for software in data:
                    csv_row = create_csv_data(software, filename_without_ext)
                    csv_data.append(csv_row)

                # Write data to CSV file
                with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                    writer = csv.writer(csv_file)
                    # Write header
                    writer.writerow([
                        "Post Content",
                        "Dashboard Image URL",
                        "Website Link",
                        "Hashtags",
                        "Features Highlights",
                        "Description",
                        "Title"
                    ])
                    # Write rows
                    writer.writerows(csv_data)

            print(f"CSV file created: {csv_file_path}")

if __name__ == "__main__":
    process_json_files()
