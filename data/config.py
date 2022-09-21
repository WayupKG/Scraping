from environs import Env

env = Env()
env.read_env()

url = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/"
url_end = 'c37l1700273'

not_image = "https://afs.googleusercontent.com/kijiji-ca/csa-image1-large.png"

headers = {
    "Accept": "*/*",
    "User-Agent":  env.str("USER_AGENT")
}


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = "credentials.json"
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = "1kNKv6cvQeUidCEEQCrSWdwHOT0FxaCeJ0eQbrEzg_RE"
