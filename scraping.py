import sys
from bs4 import BeautifulSoup
from requests import get

def get_pageid():
    if len(sys.argv) < 2 or int(sys.argv) == 0:
        return 1
    else: 
        return int(sys.argv[1])

def get_news():  
    url = f'https://www.leme.sp.gov.br/noticias/{get_pageid()}'
    req = get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup.find_all('div', class_='box-noticia row')

class NewsBox:
    newsbox = None
    def __init__(self, newsbox):
        self.newsbox = newsbox

    def __get_text_container(self):
        return self.newsbox.find('div', class_='box-noticia__texto-container')

    def get_title(self):
         return self.__get_text_container().find('h4').next_element

    def get_description(self):
        return ' '.join(self.get_title().next_element.split())

    def get_pub_date(self):
        return self.__get_text_container().find('img', class_='calendar-icon').next_element.strip()


news = list(map(NewsBox, get_news()))

for new in news:
    print(
        f"""
{new.get_title()}

{new.get_description()}

{new.get_pub_date()}
--------------------------------------"""
    )
