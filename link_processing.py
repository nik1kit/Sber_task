from bs4 import BeautifulSoup
from essence_of_case import essence_of_case
from common import IS_PROXIES

from selenium import webdriver
import time
from common import PLAINTIFFS, DEFENDANTS, THIRDS, OTHERS

def link_processing(links, session):
    for link in links:
        time.sleep(3)
        response = session.get(url=link)
        time.sleep(3)
        soup = BeautifulSoup(response.text, "lxml")
        print(soup)
        # истец
        plaintiff = soup.find_all("td", class_="plaintiffs")[1]
        if plaintiff != None:
            new_plaintiff = plaintiff.find("a")
            if new_plaintiff != None:
                PLAINTIFFS.append(plaintiff.text.rstrip().lstrip())
            else:
                PLAINTIFFS.append(f"-")
        else:
            PLAINTIFFS.append(f"-")
        # ответчик
        defendant = soup.find_all("td", class_="defendants")[1]
        if defendant != None:
            new_defendant = defendant.find("a")
            if new_defendant != None:
                DEFENDANTS.append(defendant.text.rstrip().lstrip())
            else:
                DEFENDANTS.append(f"-")
        else:
            DEFENDANTS.append(f"-")
        # третьи лица
        third = soup.find_all("td", class_="third")[1].find_all("a")
        thirds = []
        if third != None:
            for item in third:
                thirds.append(
                    item.text.rstrip().lstrip()
                ) if third is not None else THIRDS.append(f"-")
        else:
            thirds.append(f"-")
        THIRDS.append(thirds)
        # другие лица
        other = soup.find_all("td", class_="others")[1].find_all("a")
        others = []
        if other != None:
            for item in other:
                others.append(
                    item.text.rstrip().lstrip()
                ) if item is not None else OTHERS.append(f"-")
        else:
            others.append(f"-")
        OTHERS.append(others)

        essence_of_case(soup)
