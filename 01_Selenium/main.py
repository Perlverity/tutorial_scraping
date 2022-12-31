import chromedriver_binary # <- これでChromeDriverをPATHに自動追加してくれる
from selenium import webdriver


driver = webdriver.Chrome()

url = 'https://github.com/Perlverity'
path = '.p-name.vcard-fullname.d-block.overflow-hidden'

driver.get(url)

title_elem = driver.find_element_by_css_selector(path).text
print(title_elem)
