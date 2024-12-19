import sys
sys.path.append('../Football_Analysis')
from src.objects.web_scraping import WebScraping
import pandas as pd

def extract_data(**kwargs):
    """
    Extracts data from the webpage
    """
    # Setup variables
    url = kwargs['url']
    target_table_index = kwargs['target_table_index']
    target_table = []
    ws = WebScraping(url)
    table_elements = ws.get_html_element('table')


    for table in table_elements:
        target_table.append(pd.read_html(str(table))[0])
    return target_table[target_table_index].to_csv("./data/stadiums.csv", index=False)

kwargs = {"url": "https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity", "target_table_index": 2}
print(extract_data(**kwargs))
    