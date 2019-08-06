from bs4 import BeautifulSoup
import requests
from requests import get
page = requests.get(raw_input("Enter URL: "))
html = page.text
soup = BeautifulSoup(html, "html.parser")
body = soup.find("div", attrs={'class': 'sclt-feed-uncover'})

for link in body.find_all('a'):
    print(link)
    url = link.get('href')
    if ".mp3" in url:
        print(url)
        with open(url, "wb") as file:
            response = get(domain + url)
            file.write(response.content)
    else:
        continue
