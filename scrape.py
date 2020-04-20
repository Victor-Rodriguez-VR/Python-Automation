import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
for i in range (len(quotes)):
    quoteTags = tags[i].find_all('a', class_='tag')
    print(quotes[i].text + ' - ' + authors[i].text + ' with tags ')
    for quoteTag in quoteTags:
        print(quoteTag.text)
