from bs4 import BeautifulSoup
import requests
from requests import get

page = requests.get(raw_input("Enter URL: "))
filetype = '.' + raw_input("Enter File Extension (with no dot):")
html = page.text
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all('a'):
    url = link.get('href')
    if filetype in url:
        print(url)
        with open(url, "wb") as file:
            response = get(domain + url)
            file.write(response.content)
    else:
        continue
