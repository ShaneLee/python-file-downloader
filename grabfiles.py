#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from requests import get

page = requests.get(input('Enter URL: '))
filetype = '.' + input('Enter File Extension (with no dot): ')
soup = BeautifulSoup(page.text, 'html.parser')

for link in soup.find_all('a'):
    url = link.get('href')
    if filetype in url:
        print(url)
        with open(url, 'wb') as file:
            response = get(url)
            file.write(response.content)
    else:
        continue
