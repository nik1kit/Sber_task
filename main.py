from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time
from get_link_on_case import scrap_inf

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-blink-features=AutomationControlled')




driver = webdriver.Chrome(options=options)
URL = "https://kad.arbitr.ru"


driver.get(URL)
time.sleep(5)

data_first = "01.06.2024"
data_second = "30.06.2024"

data_input = driver.find_elements(By.CSS_SELECTOR, 'input[class="anyway_position_top g-ph"]')
data_first_input = data_input[0]
data_second_input = data_input[1]
data_first_input.click()
time.sleep(3)
data_first_input.send_keys(data_first)
time.sleep(5)

data_second_input.click()
time.sleep(3)
data_second_input.send_keys(data_second)
time.sleep(3)
data_second_input.send_keys(Keys.RETURN)
time.sleep(5)

Page_source = driver.page_source
soup = BeautifulSoup(Page_source, 'lxml')
scrap_inf(soup)
time.sleep(5)
driver.close()


