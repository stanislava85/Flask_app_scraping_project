import requests
from bs4 import BeautifulSoup

#url = 'https://worldpopulationreview.com/country-rankings/maternity-leave-by-country'  

def mat_leave(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    table = soup.find("table") 
    rows = table.find_all('tr')
    th_td_list = []
    for row in rows:
        th = row.findAll('th')
        tds = row.findAll('td')
        th_td_data_row = []
        for td in tds:
            td_text = td.text.strip()
            td_text = td_text.replace(',',"")
            if td_text == '':
                td_text = 0.0      
            else:
                td_text = td_text
            th_td_data_row.append(td_text)              
        th_td_list.append(th_td_data_row)
        th_td_list[0] = ["Country", "Weeks Paid", "Payment Rate", "Population 2020"]
    output_list = []
    for l in th_td_list[1:]:
        output_list.append([l[0],float(l[1]),float(l[2][:-1]),int(l[3])])
    #print(output_list)
    return(output_list)
    

#mat_leave("https://worldpopulationreview.com/country-rankings/maternity-leave-by-country")

