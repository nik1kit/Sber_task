from common import ESSENCE_OF_CASE


def essence_of_case(html_code):
    soup = html_code.find("div", class_="js-chrono-items-wrapper")
    all_information = soup.find_all("div", class_="r-col")
    all_information_dict = []
    for item in all_information:
        information = item.find("span", class_="js-judges-rollover")
        if information != None:
            all_information_dict.append(information.text.rstrip().lstrip())
        else:
            all_information_dict.append(f"-")
    ESSENCE_OF_CASE.append(all_information_dict)