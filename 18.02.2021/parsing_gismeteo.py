import requests
from bs4 import BeautifulSoup
import json

HOST = 'https://www.gismeteo.ua/'
URL = 'https://www.gismeteo.ua/weather-moscow-4368/10-days/'
HEADERS = {
    'accept': (
        'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    ),
    'user-agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/88.0.4324.150 Safari/537.36'
    ),
}


def get_html(url, params=""):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    cards = []
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='widget__wrap')

    # Получаем списки элементов каждого типа
    day_items = items.find_all('div', class_='w_date')
    min_temp_items = items.find_all('div', class_='maxt')
    max_temp_items = items.find_all('div', class_='mint')

    for i in zip(day_items, min_temp_items, max_temp_items):
        date = i[0].find('span', 'w_date__date black') or i[0].find('span', 'w_date__date weekend')
        cards.append(
            {
                'day_of_week': i[0].find('div', class_='w_date__day').get_text(),
                'date': date.get_text(strip=True),
                'min_temp': i[1].find('span', class_='unit unit_temperature_c').get_text(),
                'max_temp': i[2].find('span', class_='unit unit_temperature_c').get_text(),
            }
        )

    return cards


html = get_html(URL)
content = get_content(html.text)
content = json.dumps(content, ensure_ascii=False)

with open('../days.txt', 'w') as f:
    f.write(content)
