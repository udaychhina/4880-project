import requests
import json
import os
import time
import random

api_key = "BqcW5aiOCB5grbROZbdKaGNnBeKX61xy"
years = [2023, 2024]
months = range(1, 9)  # Months 1 to 12
num_requests = 4  # Number of random months to select

# Ensure the directory for storing files exists
os.makedirs("NYT_Articles", exist_ok=True)

for _ in range(num_requests):
    year = random.choice(years)
    month = random.choice(months)
    url = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Define the filename based on the year and month
        file_name = f"NYT_Articles/articles_{year}_{month}.json"

        # Save the data to a new file
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Data for {year}-{month} saved to {file_name}")
    else:
        print(f"Failed to retrieve data for {year}-{month}: {response.status_code}")

    # Add a delay of 5 seconds between requests
    time.sleep(5)

print("Data retrieval complete!")
