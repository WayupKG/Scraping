import csv
import requests
import re

from datetime import date
from bs4 import BeautifulSoup

from data.config import url, url_end, not_image, headers

from service import save_google_sheets
        
def get_house(response):
    soup = BeautifulSoup(response.text, 'lxml')
    houses = soup.find("main").find_all("div", class_="search-item")
    page_data = []
    for item in houses:
        title = item.find("a", class_="title").text.strip(),
        price = item.find("div", class_="price").text.strip(),
        date = item.find("div", class_="location").find('span', class_="date-posted").text.strip(),
        image_ = item.find("img").get("data-src")
        image = image_ if image_ is not None else not_image
        page_data.append([title[0], price[0], date[0], image])
    return page_data


def get_page_houses(page: int):
    data = []
    for i in range(1, page):
        full_url = f"{url}page-{i}/{url_end}"
        req = requests.get(full_url, headers=headers)
        req_page = re.findall(r'\d{1}/|\d{2}/', req.url)
        current_page = int(req_page[0].replace('/', '')) if req_page else 1

        print(f"current_page = {current_page} | page = {i}")
        data.extend(get_house(req))

        if current_page != i:
            print("Страница было перенаправлено")
            break
    save_google_sheets.save(data)


def main(): 
    get_page_houses(10)