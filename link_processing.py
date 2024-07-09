from bs4 import BeautifulSoup
from fake_useragent import UserAgent

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
        driver.get(link)
        time.sleep(5)
        Page_source = driver.page_source
        soup = BeautifulSoup(Page_source, 'lxml')
        # истец
        plaintiff = soup.find('td', class_="plaintiffs first").find('a').text
        PLAINTIFFS.append(plaintiff)
        #ответчик
        defendant = soup.find_all('td', class_="defendants")[1].find('a').text
        DEFENDANTS.append(defendant)
        # третьи лица
        third = soup.find_all('td', class_="third")[1].find_all('a')
        thirds = []
        if third != None:
            for item in  third:
                thirds.append(item.text) if third is not None else THIRDS.append('-')
        else:
            thirds.append('-')
        THIRDS.append(thirds)
        # другие лица
        other = soup.find_all('td', class_="others")[1].find_all('a')
        others = []
        if other != None:
            for item in other:
                others.append(item.text) if item is not None else OTHERS.append('-')
        else:
            others.append('-')
        OTHERS.append(others)
        print(PLAINTIFFS)
        print(DEFENDANTS)
        print(THIRDS)
        print(OTHERS)
        break

