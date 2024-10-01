from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

obj = UserAgent()
header = {'user-agent': obj.chrome}
# API_KEY = "AKvMMl7Zo5PeHpeiITEPHvkTV"
# API_SECRET_KEY = "wYmnt4frB8qDAKWsUlnBJELPfj2ogAtHgbz6QkeNDasf5wvzLd"
# ACCESS_TOKEN = "1740341581314437120-H1348jgTiGK79sen6hJJZg0Pe8mpei"
# ACCESS_TOKEN_SECRET = "QdN4WvpNgB6rMPAAbdeIkTc4qe5aPjG6fJFvLq5Z9gipl"

url = 'https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python'
# TODO: url = rss
response = requests.get(url)
html = response.content
# req = requests.get(url, headers=header)
soup = BeautifulSoup(html, 'html.parser')

# for _ in soup:
#     print(_)
print(soup.get_text())