import requests

API_URL = 'https://api.restful-api.dev/objects'
search_id = input("enter the id from 1 to 12: ").strip()
response = requests.get(API_URL)
data = response.json()

for item in data:
    if item["id"] == search_id:
        print("product name:", item["name"])

        if "Generation" in item["data"]:
            print("Generation:", item["data"]["Generation"])
        else:
            print("Generation: not available")

        if "Price" in item["data"]:
            print("Price:", item["data"]["Price"])
        else:
            print("Price: Price is not shown!")

        break
else:
    print("id not found")
