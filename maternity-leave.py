#from flask import Flask
import requests
from bs4 import BeautifulSoup
import csv

# app = Flask('webapp')
url = 'https://worldpopulationreview.com/country-rankings/maternity-leave-by-country'  
page = requests.get(url)
soup = BeautifulSoup(page.content)
table = soup.find("table")

# def get_all_tables(soup):
#     """Extracts and returns all tables in a soup object"""
#     return soup.find_all("table")

#get_all_tables(soup)

def get_table_headers(table):
    """Given a table soup, returns all the headers"""
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers

#get_table_headers(table)

def get_table_rows(table):
    """Given a table, returns all its rows"""
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows


def data_to_csv(URL):
    with open("stanislava-maternity-leave.csv", "w") as csvfile:
        file = csv.writer(csvfile)
        file.writerow(["Country","Weeks Paid",'Payment Rate', 'Population 2020'])
        file.writerows(get_table_rows(table))
        
data_to_csv(url)

