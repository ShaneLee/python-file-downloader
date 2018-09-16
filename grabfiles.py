from bs4 import BeautifulSoup
import requests
from requests import get
domain = "http://purehumbug.com"
page = requests.get("http://purehumbug.com/shows/2006/1-99/")
html = page.text
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all('a'):
    url = link.get('href')
    if ".mp3" in url:
        print(url)
        file_name = url.split("1-99/", 1)[1]
        with open(file_name, "wb") as file:
            response = get(domain + url)
            file.write(response.content)
    else:
        continue
