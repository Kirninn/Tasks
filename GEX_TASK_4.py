import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, date, time, timedelta
import os


URL = 'https://apod.nasa.gov/apod/archivepix.html'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
          (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
          'accept': '*/*'}

html_for_parse = requests.get(URL, headers = HEADERS)

os.mkdir(r'C:\Users\Kirninn\Work\tutorial\Astronomy Picture of the Day Archive')

date_articles_last_year = []

def get_count(html):
    global date_articles_last_year
    soup = BeautifulSoup(html.text, 'html.parser')
    items = str(soup.body.find_all('b')[1]).replace('\n', '').replace('</a>', '').replace('</b>', '').replace('<b>', '').strip().split('<br/>')
    items.remove('')

    date_articles = []

    for item in items:
        date_articles.append({
        'date_art': datetime.strptime((re.search(r'\d{4} [a-zA-Z]+ \d{1,2}', item).group()),'%Y %B %d'),
        'link_art': re.findall(r'href=[\'"]?([^\'" >]+)', item)
        })

    year_find = datetime.now() - timedelta(days=365)

    for keys in date_articles:
        if keys['date_art'] >= year_find:
            keys['date_art'] = keys['date_art'].strftime('%Y-%m-%d')
            date_articles_last_year.append(keys)

get_count(html_for_parse)

for item in date_articles_last_year:
    root = r'C:\Users\Kirninn\Work\tutorial\Astronomy Picture of the Day Archive'
    dir_path = os.path.join(root, item['date_art'])
    os.makedirs(dir_path)
    file_path = os.path.join(dir_path, f"{item['date_art']}.txt")

    url = 'https://apod.nasa.gov/apod/' + (''.join(item['link_art']))
    requests_print = requests.get(url)

    soup = BeautifulSoup(requests_print.text, 'html.parser')
    text_article = str(soup.body.find_all('p')[2].get_text()).strip().split("Tomorrow's")

    list_article = []

    for item in text_article:
        list_article.append(item)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(list_article[0])

    search = soup.find('img')
    if (search is None):
        continue
    else:
        img_src = soup.find('img')['src']
        url_image = 'https://apod.nasa.gov/apod/' + img_src

        response_image = requests.get(url_image)

        with open(os.path.join(dir_path, 'image_of_day.jpg'), 'wb') as imgfile:
            imgfile.write(response_image.content)
