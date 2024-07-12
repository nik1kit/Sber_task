from common import DATE


def get_date(html_code):
    all_date = html_code.find_all("td", class_="num")
    for item in all_date:
        date = item.find("span")
        if date != None:
            DATE.append(date.text.replace("\n", "").replace(" ", ""))
        else:
            DATE.append(f"-")
