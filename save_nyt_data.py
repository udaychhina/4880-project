import json
import requests
import time


API_KEY = '4X3YJCiufGwCWyTYonHgnOcmMh3vqFfV'

def get_nyt_articles(year, month):
    url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={API_KEY}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['response']['docs']

def build_nyt_archive():
    articles = []
    month = 1
    for year in range(2013, 2023):
        articles.extend(get_nyt_articles(year, month))
        print(f'Fetched {len(articles)} articles total.')
        time.sleep(10)
    return articles

def save_nyt_archive(articles):
    with open('data/nyt_archive_2013_2023_jan.json', 'w') as f:
        json.dump(articles, f)


if __name__ == '__main__':
    articles = build_nyt_archive()
    save_nyt_archive(articles)
    print('NYT archive saved to nyt_archive_2013_2023_jan.json')
