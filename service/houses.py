import requests
import re

from bs4 import BeautifulSoup

from data.config import url, url_end, not_image, headers

from service import save_house_db
from service import save_house_google_sheets



def get_house(response):
    soup = BeautifulSoup(response, 'lxml')
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


def get_response_page(page: int):
    full_url = f"{url}page-{page}/{url_end}"
    response = requests.get(full_url, headers=headers)
    response_page = re.findall(r'\d{1}/|\d{2}/', response.url)
    current_page = int(response_page[0].replace('/', '')) if response_page else 1
    context = {'response': response.text, 'page': current_page}
    return context


def get_page_houses(start_page: int, end_page: int):
    data = []
    for i in range(start_page, end_page + 1):
        response_page = get_response_page(i)
        page_data = get_house(response_page['response'])
        data.extend(page_data)
        print(f"\nПолучено данные страницы = {i}")
    return data


def main():
    while True:
        print("\nВыберите куда вам надо сохранить результаты парсера\n1) На базу данных\n2) На Google Sheet")
        answer_user = input("напишите цифру - ")
        if answer_user.isdigit() and int(answer_user) in [1,2]:
            while True:
                print("\nУкажите диапазон страницы")
                start_page, end_page = input("начало страницы - "), input("конец страницы - ")
                if start_page.isdigit() and end_page.isdigit():
                    data_houses = get_page_houses(int(start_page), int(end_page))
                    match int(answer_user):
                        case 1:
                            save_house_db.save(data_houses)
                        case 2:
                            save_house_google_sheets.save(data_houses)
                    break
                print("\nУкажите корректные данные")
            break
            
                    
                