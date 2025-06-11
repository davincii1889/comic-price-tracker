import os
import requests
from dotenv import load_dotenv

# Load your eBay API key from the .env file
load_dotenv()
APP_ID = os.getenv("AbdoulTo-ComicPri-SBX-0472db649-a045d14b")

# Function to fetch recent ungraded comic book listings from eBay
def fetch_ungraded_comics(query="Spider-Man Comic", entries=10):
    endpoint = "https://svcs.ebay.com/services/search/FindingService/v1"
    params = {
        "OPERATION-NAME": "findCompletedItems",
        "SERVICE-VERSION": "1.0.0",
        "SECURITY-APPNAME": APP_ID,
        "RESPONSE-DATA-FORMAT": "JSON",
        "REST-PAYLOAD": "",
        "keywords": query,
        "categoryId": "63",  # Category ID for Comics
        "itemFilter(0).name": "Condition",
        "itemFilter(0).value": "Used",  # Usually used = ungraded
        "itemFilter(1).name": "SoldItemsOnly",
        "itemFilter(1).value": "true",
        "paginationInput.entriesPerPage": entries
    }

    response = requests.get(endpoint, params=params)
    data = response.json()
    import json
    print(json.dumps(data, indent=2))

    try:
        items = data["findCompletedItemsResponse"][0]["searchResult"][0]["item"]
        for item in items:
            title = item["title"][0]
            price = item["sellingStatus"][0]["currentPrice"][0]["__value__"]
            currency = item["sellingStatus"][0]["currentPrice"][0]["@currencyId"]
            print(f"{title} - {price} {currency}")
    except KeyError:
        print("No items found or something went wrong.")

# Run the function
fetch_ungraded_comics("Spider-Man #1")
