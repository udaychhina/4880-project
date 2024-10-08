import json
import requests
import time
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

API_KEY = config['API_KEY']

def get_nyt_articles(year, month):
    url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={API_KEY}'
    response = requests.get(url)
    response.raise_for_status()
    # return only the articles. The response object contains metadata as well.
    return response.json()['response']['docs']

def build_nyt_archive():
    articles = []
    month = 1
    for year in range(2013, 2025):
        articles.extend(get_nyt_articles(year, month))
        print(f'Fetched {len(articles)} articles total.')
        time.sleep(10)
    return articles

def save_nyt_archive(articles):
    # check if the data folder exists, if not, create it
    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/nyt_archive_2013_2023_jan.json', 'w') as f:
        json.dump(articles, f)


if __name__ == '__main__':
    articles = build_nyt_archive()
    save_nyt_archive(articles)
    print('NYT archive saved to nyt_archive_2013_2023_jan.json')
