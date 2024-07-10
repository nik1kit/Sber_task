from common import COURTS
def get_courts(html_code):
    courts = html_code.find_all('td', class_="court")
    for item in courts:
        new_item = item.find_all('div')
        for i in new_item:
            if not i.get('class', []):
                COURTS.append(i.get('title').rstrip().lstrip())


