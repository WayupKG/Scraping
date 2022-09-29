import os

from environs import Env

env = Env()
env.read_env()

# Ссылка сайта
url = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/"
url_end = 'c37l1700273'

# Ссылка нужен для не найденных изображении
not_image = "https://afs.googleusercontent.com/kijiji-ca/csa-image1-large.png"

headers = {
    "Accept": "*/*",
    "User-Agent":  env.str("USER_AGENT")
}

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = "credentials.json"

# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = env.str("SHEET_ID")

# Настройки базы данных
DATABASE = env.str("DATABASE")
DATABASE_NAME = os.environ.get("DATABASE_NAME", 'db.sqlite3')
DATABASE_USER = os.environ.get("DATABASE_USER", "user")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "password")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "5432")

if DATABASE == 'postgresql':
    DATABASE_ENGINE = f"{DATABASE}+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}"\
                      f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
else:
    DATABASE_ENGINE = f"sqlite:///{DATABASE_NAME}"