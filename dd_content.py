import csv
import json
from operator import delitem
import random
from urllib import request

def get_random_quote(quotes_file='quotes.csv'):
    try:
        with open(quotes_file) as csvfile:
            quotes = [{'author': line[0],
                       'quote': line[1]} for line in csv.reader(csvfile, delitem-'|')]
    except Exception as e:
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always look on the bright side of life.'}]
        
    return random.choice(quotes)

def get_weather_forecast(coords={'lat': 28.4717, 'lon': -80.5378}):
    try:
        api_key = 'e9bc8124b03ecf26a93859c53de950e9'
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units='
        data = json.load(request.urlopen(url))

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass

if __name__ == '__main__':
    print('Testing quote generation.\n')

    quote = get_random_quote()
    print(f' -Random quote is "{quote["quote"]}" - {quote["author"]}')

    quote = get_random_quote(quotes_file=None)
    print(f' -Default quote is "{quote["quote"]}" - {quote["author"]}')