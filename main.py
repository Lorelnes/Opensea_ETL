import csv
from extract import get_collections_with_pagination

# Initialize file counter
file_counter = 1

# Define a function to create CSV files
def create_csv_file(collections, chain, page, has_next):
    global file_counter
    filename = f"{chain}-page-{page}-{'next' if has_next else 'last'}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['collection', 'name', 'description', 'image_url', 'owner', 'twitter_username', 'contracts'])
        for collection in collections:
            writer.writerow([
                collection.get("collection"),
                collection.get("name"),
                collection.get("description"),
                collection.get("image_url"),
                collection.get("owner"),
                collection.get("twitter_username"),
                collection.get("contracts")
            ])
    print(f"Data has been written to {filename}")

# Call the function to start retrieving collections
get_collections_with_pagination()
