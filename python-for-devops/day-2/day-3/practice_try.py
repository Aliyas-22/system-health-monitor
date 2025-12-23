import requests
import json
 

try:
    API_URL = 'https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873'
    time = input("what you want to see sunset , sunrise , date : ").strip().lower()
    response = requests.get(API_URL)
    output = response.json()
    
    with open("sun_data.json", "r") as file:
         stored_data = json.load(file)

    # with open("sun_data.json", "w") as file:
    #     json.dump(output, file, indent=4)
    print("API data read successfully into sun_data.json")
    # print("API data saved successfully into sun_data.json")
    results = output["results"]
    date = results["date"]
    first_light = results["first_light"]
    if time in results :
            print(f"{time.capitalize()} time is :, {results[time]}")
            # if time in date :
            #     print(f"{date.capatalize()} date is :,{date[time]}")
    else:
        print("invalid input, please enter properly!")
    # print(results)
except Exception as e:
    print("Error:", e)