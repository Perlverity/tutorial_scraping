from bs4 import BeautifulSoup as bs4
import requests


url = 'https://github.com/Perlverity'
path = 'span'

res = requests.get(url)

soup = bs4(res.text, 'html.parser')

# print(soup.prettify())

# for element in soup.find_all(path):
#     print(element.text)

element = soup.find(class_='vcard-names')
print(element)

for element_val in element.find_all('span'):
    print(element_val.text)