import os
import csv
import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from slugify import slugify
from scrap_book import scrap_book


# Etape 2 : Extraire toutes les données des produits d'une catégorie :
# Cette fonction nous permet d'obtenir une liste de tous les liens
# des livres de la catégorie sur une ou plusieurs pages.
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

        # pagination
        next_page_element = soup.select_one('li.next > a')

        if next_page_element:
            next_page_url = next_page_element.get('href')
            url = urljoin(url, next_page_url)

        else:
            break

    return all_book_links


# On charge une liste de dictionnaire dans un fichier csv.
def scrap_category_books(book_links):
    books_data = [scrap_book(elm, load=False) for elm in book_links]
    headers = books_data[0].keys()
    category_name = books_data[0]["category"]
    path_category = "all_books/" + category_name
    path_images = path_category + "/images"
    os.makedirs(path_images, exist_ok=True)
    category_csv = path_category + "/" + slugify(category_name) + ".csv"

    with open(category_csv, 'w', encoding="utf-8-sig", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter='|')
        writer.writeheader()

    for dic in books_data:
        path_book_image = path_images + "/" + slugify(dic["title"]) + ".jpg"
        if not os.path.isfile(path_book_image):
            response = requests.get(dic["image_url"])
            file = open(path_book_image, "wb")
            file.write(response.content)
            file.close()

        with open(category_csv, 'a', encoding="utf-8-sig", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter='|')
            writer.writerow(dic)


# Ici, on applique la fonction précédente à notre liste contenant les url de tous les livres de la catégorie.
def scrap_category(url_category):

    all_links = get_links_category(url_category)
    scrap_category_books(all_links)


if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
    t1 = time.time()
    scrap_category(url)
    t2 = time.time()
    print("Temps ecoulé: ", t2 - t1)



