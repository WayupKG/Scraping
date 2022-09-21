Парсинг сайта [Kijiji](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273).
==================================

#### ВНИМАНИЕ! Этот проект предназначен только для локального тестирования, он не подготовлен к развертыванию на удаленном сервере.
<hr>

# Инструкция

- ## Кланируйте этот проект 
```
$ git clone https://github.com/WayupKG/Scraping
```

- ##  Установите ``Poetry`` для управления зависимостями и сборкой пакетов в Python 
- ## Установите необходимые зависимости
```
$ poetry install
```
- ## Переименуйте файл ``.env.dist`` на ``.env`` и изменить содержимое 
```
$ mv .env.dist .env
```

- ## Создайте таблицу в ``Google Disk (Google Диск)`` и дайте доступ для этой почты 
```
xxx-333@myscraping-363206.iam.gserviceaccount.com
```

- ## Скапируйте id таблицы `(1kNKv6cvQsdUisddCEEQCsdSWdwHOT0FxaCeJ0eQbrEzg_RE)`
```
https://docs.google.com/spreadsheets/d/ тут будет id таблицы /edit#gid=0
```

- ## Измените `USER_AGENT` в файле `.env`
```
USER_AGENT = тут должен быть ваш USER_AGENT
```
#### Если вы не знакомы с `User-Agent'ом` то тут вы можете узнать [подробнее](https://trofimovdigital.ru/blog/user-agent).


- ## Измените `SHEET_ID` в файле `.env`
```
SHEET_ID = тут должен быть id вашей таблицы
```


- ## Активируйте виртуальное окружение
```
$ poetry shell
```

- ## И запустите проект
```
$ python3 app.py
```
<br><hr>

## Ссылка на [Google Sheet](https://docs.google.com/spreadsheets/d/1kNKv6cvQeUidCEEQCrSWdwHOT0FxaCeJ0eQbrEzg_RE/edit#gid=0).