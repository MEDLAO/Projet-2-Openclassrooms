import csv
from pprint import pprint
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from scrap_category import *
# Etape 3 : Extraire tous les produits de toutes les catégories :
def etl_categories(home_url):
    page = requests.get(home_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    categories_links = [home_url + url_category.get('href') for url_category in soup.select('div ul li a')[:-1]]

    for category_link in categories_links[2:]:
        scrap_category(category_link)



# Ce code s'éxécute seulement si je fais >>> python scrap_all_categories.py dans le terminal
if __name__ == "__main__":
    home_url = "https://books.toscrape.com/"
    etl_categories(home_url)