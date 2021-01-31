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

date_articles_last_year = []

def get_count(html):
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
        url = 'https://apod.nasa.gov/apod/' + (''.join(keys['link_art']))
        requests_have_image = requests.get(url)
        soup_have_image = BeautifulSoup(requests_have_image.text, 'html.parser')
        search = soup_have_image.find('img')
        if (search is not None):
            if keys['date_art'] >= year_find:
                keys['date_art'] = keys['date_art'].strftime('%Y-%m-%d')
                date_articles_last_year.append(keys)
            else:
                break

get_count(html_for_parse)

def get_text_and_image():

    os.mkdir(r'C:\Users\Kirninn\Work\tutorial\Astronomy Picture of the Day Archive')

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

        img_src = soup.find('img')['src']

        response_image = requests.get('https://apod.nasa.gov/apod/' + img_src)

        with open(os.path.join(dir_path, 'image_of_day.jpg'), 'wb') as imgfile:
            imgfile.write(response_image.content)

get_text_and_image()
