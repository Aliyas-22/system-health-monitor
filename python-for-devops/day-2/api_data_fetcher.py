import requests
import json


API_URL = 'https://api.restful-api.dev/objects'
search_id = (input("enter the id from 1 to 12:  ").strip())
response = requests.get(API_URL)


data = response.json()

for item in data:
    if item ["id"] == search_id:
        product_data = {}
        product_data["name"] = item["name"]
        print(product_data)

        print("product name:",item["name"])
        if "Generation" in item["data"]:
            product_data["Generation"] = item["data"]["Generation"]
            # print("Generation:", item["data"]["Generation"])
            print(product_data)
        else:
            product_data["Generation"] = "not available"
            

            # print("Generation: not available")
        if "Price" in item["data"]:
            # print("Price:",item["data"]["Price"])
            product_data["Price"] = item["data"]["Price"]
            print(product_data)

        else:
            product_data["Price"] = "not available"
            # print("Price:Price is not shown!")

        break
else:
 print("id not found")