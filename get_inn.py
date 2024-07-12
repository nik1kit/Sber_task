from common import INN


def get_inn(html_code):
    inn_plaintiff = html_code.find_all("td", class_="plaintiff")
    inn_respondent = html_code.find_all("td", class_="respondent")
    inn_respondent_dict = []
    inn_plaintiff_dict = []
    for item in inn_plaintiff:
        inn_ = item.find("span", class_="js-rolloverHtml").find("div")
        if inn_ != None:
            inn_plaintiff_dict.append(inn_.text.replace("\n", "").replace(" ", "")[4:])
        else:
            inn_plaintiff_dict.append(f"-")

    for item in inn_respondent:
        inn_ = item.find("span", class_="js-rolloverHtml").find("div")
        if inn_ != None:
            inn_respondent_dict.append(inn_.text.replace("\n", "").replace(" ", "")[4:])
        else:
            inn_respondent_dict.append(f"-")

    for index in range(len(inn_plaintiff_dict)):
        INN.append([inn_plaintiff_dict[index], inn_respondent_dict[index]])
