import requests
import json


url = "https://api.nytimes.com/svc/archive/v1/2024/1.json?api-key=BqcW5aiOCB5grbROZbdKaGNnBeKX61xy"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Load existing data from the file if it exists
    try:
        with open('articles.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Append new data
    existing_data.append(data)

    # Save updated data back to the file
    with open('articles.json', 'w') as file:
        json.dump(existing_data, file, indent=4)
else:
    print(f"Failed to retrieve data: {response.status_code}")
