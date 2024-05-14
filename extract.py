import requests

# Define the API endpoint URL
url = "https://api.opensea.io/api/v2/collections"

# Adding API key to the headers
headers = {
    "Accept": "application/json",
    "X-API-KEY": "dacdcd35228a40638599c4c33ceb4a74"
}

def get_collections_with_pagination():
    params = {
        "chain": "ethereum"
    }
    page = 1
    while True:
        params["page"] = page
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            collections = data.get("collections", [])
            has_next = data.get("next", None) is not None
            from main import create_csv_file
            create_csv_file(collections, params["chain"], page, has_next)
            if not has_next:
                break
            page += 1
        else:
            print("Error retrieving collections:", response.status_code)
            break
