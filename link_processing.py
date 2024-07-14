from bs4 import BeautifulSoup
from essence_of_case import essence_of_case

from selenium import webdriver
import time
from common import PLAINTIFFS, DEFENDANTS, THIRDS, OTHERS


def link_processing(links, session):
    for link in links:
        time.sleep(5)
        response = session.get(link)
        soup = BeautifulSoup(response.text, "lxml")
        # истец
        plaintiff = (
            soup.find_all("td", class_="plaintiffs")[1].find("a").text.rstrip().lstrip()
        )
        PLAINTIFFS.append(plaintiff)
        # ответчик
        defendant = soup.find_all("td", class_="defendants")[1].find("a")
        DEFENDANTS.append(defendant.text.rstrip().lstrip())
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
