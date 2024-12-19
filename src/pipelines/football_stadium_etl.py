from bs4 import *
import requests
import pandas as pd


def fetch_url_html(url):
    """
    Returns the HTML content of a given URL
    """
    try:
        response = requests.get(url).text
        return response
    except requests.RequestException as e:
        print(f"An error occured: {e}")

def get_table(response) -> BeautifulSoup:
    """
    Returns all tables in the HTML content
    """
    soup = BeautifulSoup(response, 'html.parser')
    tables = soup.find_all('table')
    return tables

def get_img_url(tables):
    """
    Returns the URL of the images in the HTML content
    """
    soup = BeautifulSoup(str(tables[table_index]), 'html.parser')
    rows = soup.find_all('tr')
    image_urls = []

    for row in rows:
        img = row.find('img')
        if img:
            # Construct the full URL for the image
            img_url = f"https://upload.wikimedia.org{img['src']}"
        else:
            img_url = None
        image_urls.append(img_url)

def get_target_table(tables: BeautifulSoup, table_index: int) -> pd.DataFrame:
    """
    Returns target table

    Args:
        tables: BeautifulSoup object
        table_index: index of the target table

    Returns:
        pd.DataFrame: target table
    """
    dfs = []
    for table in tables:
        dfs.append(pd.read_html(str(table))[0])
    return dfs[table_index]

url = r"https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"
response = fetch_url_html(url)
table = get_table(response)
df = get_target_table(table, 2)
df.to_csv("data/football_stadiums.csv", index=False)