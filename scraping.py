from bs4 import BeautifulSoup
from requests import get

url = 'https://www.leme.sp.gov.br/noticias'
req = get(url)
soup = BeautifulSoup(req.content, 'html.parser')
news_boxes = soup.find_all('div', class_='box-noticia row')

news_boxes_title = []
for news_box in news_boxes:
    news_boxes_title.append(news_box.find('div', class_='box-noticia__texto-container').find('h4'))

for new_box_title in news_boxes_title:
    title = new_box_title.next_element
    content = title.next_element
    print(f'{title}\n')
    print(' '.join(content.split()))
    print('-------------------')
