from bs4 import BeautifulSoup
import requests
from requests import get

page = requests.get("https://www.cbc.ca/radio/podcasts/current-affairs-information/uncover/")
html = page.text
soup = BeautifulSoup(html, "html.parser")
body = soup.find("div", attrs={'class': 'sclt-feed-uncover'}).find_all("p")

filename = ""

for element in body:
    if element.find("strong"):
        filename = element.find("strong").text.replace("- ", "").replace(":", "").replace(" ", "_") + ".mp3"
    if element.find("a"):
        link = element.find("a")
        print(filename)
        url = link.get('href')
        if ".mp3" in url:
            print(url)
            with open(filename, "wb") as file:
                response = get(url)
                file.write(response.content)
        else:
            continue
