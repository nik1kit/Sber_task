from link_processing import link_processing
from get_inn import get_inn
from get_courts import get_courts
from get_number_of_case import get_number_of_case
from get_date_of_case import get_date


def scrap_inf(html_code, session):
    links_in_main_case = html_code.find_all("a", class_="num_case")
    links_case = []

    for item in links_in_main_case:
        case_url = item.get("href")
        links_case.append(case_url)  
    get_courts(html_code)
    get_inn(html_code)
    get_date(html_code)
    get_number_of_case(html_code)
    link_processing(links_case, session)
