from link_processing import link_processing
def scrap_inf(html_code):
    links_in_main_case = html_code.find_all('a', class_="num_case")
    links_case=[]
    for item in links_in_main_case:
        case_url = item.get('href')
        links_case.append(case_url)
    link_processing(links_case)

