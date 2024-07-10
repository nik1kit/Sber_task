from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from essence_of_case import essence_of_case

from selenium import webdriver
import time
from common import PLAINTIFFS, DEFENDANTS, THIRDS, OTHERS
def link_processing(links):
    useragent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    for link in links:
        # Разворачиваем окно браузера на весь экран
        driver.maximize_window()
        driver.get(link)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,
                            'div[title="Нажмите, чтобы ознакомиться с полной хронологией дела."]').click()

        time.sleep(3)
        Page_source = driver.page_source
        soup = BeautifulSoup(Page_source, 'lxml')
        # истец
        plaintiff = soup.find('td', class_="plaintiffs first").find('a').text.rstrip().lstrip()
        PLAINTIFFS.append(plaintiff)
        #ответчик
        defendant = soup.find_all('td', class_="defendants")[1].find('a')
        DEFENDANTS.append(defendant.text.rstrip().lstrip())
        # третьи лица
        third = soup.find_all('td', class_="third")[1].find_all('a')
        thirds = []
        if third != None:
            for item in  third:
                thirds.append(item.text.rstrip().lstrip()) if third is not None else THIRDS.append(f"-")
        else:
            thirds.append(f"-")
        THIRDS.append(thirds)
        # другие лица
        other = soup.find_all('td', class_="others")[1].find_all('a')
        others = []
        if other != None:
            for item in other:
                others.append(item.text.rstrip().lstrip()) if item is not None else OTHERS.append(f"-")
        else:
            others.append(f"-")
        OTHERS.append(others)

        essence_of_case(soup)
    driver.quit()
