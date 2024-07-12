from common import ESSENCE_OF_CASE


def essence_of_case(html_code):
    soup = html_code.find("dl", class_="b-iblock b-iblock_lightgrey").find("span")
    if soup != None:
        ESSENCE_OF_CASE.append(soup.text.rstrip().lstrip())
    else:
        ESSENCE_OF_CASE.append(f"-")

