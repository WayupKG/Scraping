import time
import asyncio
import aiohttp

from bs4 import BeautifulSoup

from data.config import url, url_end, not_image, headers

from service import save_house_db
from service import save_house_google_sheets

house_data = []
start_time = time.time()


# получает данные от определенной страницы
async def get_page_data(session, page: int) -> None:
    full_url = f"{url}page-{page}/{url_end}"
    async with session.get(url=full_url, headers=headers) as response:
        response_text = await response.text()                
        soup = BeautifulSoup(response_text, 'lxml')
        houses = soup.find_all("div", class_="search-item")
        
        for item in houses:
            title = item.find("a", class_="title").text.strip(),
            price = item.find("div", class_="price").text.strip(),
            date = item.find("div", class_="location").find('span', class_="date-posted").text.strip(),
            image_ = item.find("img").get("data-src")
            image = image_ if image_ is not None else not_image
            house_data.append([title[0], price[0], date[0], image])
        print(f"[INFO] Обработано страницы {page}")


# отрывает асинхронное соединение с сайтом
async def get_page_houses(start_page: int, end_page: int) -> None:
    async with aiohttp.ClientSession() as session:
        tasks = []
        # в каждую страницу создает асинхронное задание
        for page in range(start_page, end_page + 1):
            task = asyncio.create_task(get_page_data(session, page))
            tasks.append(task)
        await asyncio.gather(*tasks)            


# спрашивает пользователя куда хочеть сохранить результаты парсера и диапазон страницы
def main() -> None:
    while True:
        print("\nВыберите куда вам надо сохранить результаты парсера\n1) На базу данных\n2) На Google Sheet")
        answer_user = input("напишите цифру - ")
        if answer_user.isdigit() and int(answer_user) in [1,2]:
            while True:
                print("\nУкажите диапазон страницы")
                start_page, end_page = input("начало страницы - "), input("конец страницы - ")
                if start_page.isdigit() and end_page.isdigit():
                    asyncio.run(get_page_houses(int(start_page), int(end_page)))
                    match int(answer_user):
                        case 1:
                            save_house_db.save(house_data)
                        case 2:
                            save_house_google_sheets.save(house_data)
                    break
                print("\nУкажите корректные данные")
            break
    finish_time = time.time() - start_time
    print(f"\n--- Затраченное на работу скрипта время: {finish_time} ---\n")
                    
                