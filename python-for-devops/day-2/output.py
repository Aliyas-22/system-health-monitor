import json

with open("product_data.json", "r") as file:
    product_data = json.load(file)

print("Product name:", product_data["name"])
print("Generation:", product_data["Generation"])
print("Price:", product_data["Price"])
