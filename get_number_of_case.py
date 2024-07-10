from common import NUMBERS_CASE
def get_number_of_case(html_code):
    numbers_case = html_code.find_all('td', class_="num")
    for item in numbers_case:
        number_case = item.find('a')
        if number_case != None:
            NUMBERS_CASE.append(number_case.text.rstrip().lstrip())
        else:
            NUMBERS_CASE.append(f"-")
