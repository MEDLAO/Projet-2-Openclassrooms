import csv
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from scrap_book import *
import os
import urllib.request



# Etape 2 : Extraire toutes les données des produits d'une catégorie :
'''Cette fonction nous permet d'obtenir une liste de tous les liens 
   des livres de la catégorie sur une ou plusieurs pages.'''
def get_links_category(url_category):
    url = url_category
    all_book_links = []

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        book_links = [link.a['href'] for link in soup.find_all('h3')]

        for i in range(len(book_links)):
            book_links[i] = book_links[i].replace("../../../", "https://books.toscrape.com/catalogue/")

        all_book_links += book_links

        next_page_element = soup.select_one('li.next > a') # pagination

        if next_page_element:
            next_page_url = next_page_element.get('href')
            url = urljoin(url, next_page_url)

        else:
            break

    return all_book_links

# On charge une liste de dictionnaire dans un fichier csv.
def scrap_category_books(book_links):
    books_data = [scrap_book(elm) for elm in book_links]
    headers = books_data[0].keys()
    for dic in books_data:
        path_category = "all_books/" + dic["category"]
        os.makedirs(path_category, exist_ok=True)
        book_csv = path_category + "/" + slugify(dic["title"]) + ".csv"
        response = requests.get(dic["image_url"])

        file = open(path_category + "/" + slugify(dic["title"]) + ".jpg", "wb")
        file.write(response.content)
        file.close()

        with open(book_csv, 'w', encoding="utf-8-sig", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter='|')
            writer.writeheader()
            writer.writerow(dic)


# Ici, on applique la fonction précédente à notre liste contenant les url de tous les livres de la catégorie.
def scrap_category(url_category):
    all_links = get_links_category(url_category)
    scrap_category_books(all_links)


if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
    scrap_category(url)



