import csv
from pprint import pprint
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Etape 1 : Extraire les données d'un seul produit :
# Cette fonction extrait les 10 informations demandées en parsant le code html de la page choisie.
def donnees_produit(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    eparag = soup.find_all('p')
    etabl = soup.find_all('td')
    elien = soup.find_all('a')
    L = [p.get("class") for p in eparag]
    images = soup.find_all('img')
    listeimg = [item['src'] for item in images]

    product_page_url = url
    title = soup.title.string
    product_description = eparag[3].string
    universal_product_code = etabl[0].string
    price_excluding_taxe = etabl[2].string
    price_including_taxe = etabl[3].string
    number_available = etabl[5].string
    category = elien[3].string
    review_rating = L[2][1]
    image_url = listeimg[0]

    donnees = {
        "product_page_url": product_page_url,
        "title": title,
        "product_description": product_description,
        "universal_product_code": universal_product_code,
        "price_excluding_taxe": price_excluding_taxe,
        "price_including_taxe": price_including_taxe,
        "number_available": number_available,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url
    }

    return donnees

# Cette fonction modifie certains éléments obtenus.
def transform_book(donnees):
    donnees["title"] = donnees["title"].split(" | ")[0].replace("\n", "").strip()

    donnees["number_available"] = re.sub("\D+", "", donnees["number_available"])

    donnees["image_url"] = donnees["image_url"].replace("../../","https://books.toscrape.com/")

    review_rating = donnees["review_rating"]

    if review_rating == "One":
        review_rating = "1"
    elif review_rating == "Two":
        review_rating = "2"
    elif review_rating == "Three":
        review_rating = "3"
    elif review_rating == "Four":
        review_rating = "4"
    elif review_rating == "Five":
        review_rating = "5"
    donnees["review_rating"] = review_rating
    return donnees

# Charge les informations obtenues dans un fichier csv.
def load_book(donnees):
    with open('data.csv', 'w', encoding="utf-8-sig") as fichier_csv:
        writer = csv.DictWriter(fichier_csv, fieldnames=donnees.keys(), delimiter='|')
        writer.writeheader()
        writer.writerow(donnees)

# Extrait les informations demandées en prenant en compte les modifications  et les charge dans un fichier csv.
def scrap_book(url, load = True):
    donnees = donnees_produit(url)
    result = transform_book(donnees)
    if load:
        load_book(result)

    return result

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
    books_data = [scrap_book(elm, load=False) for elm in book_links]
    headers = books_data[0].keys()

    with open('livresc.csv', 'w', encoding="utf-8-sig", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter='|')
        writer.writeheader()
        for elem in books_data:
            writer.writerow(elem)

# Ici, on applique la fonction précédente à notre liste contenant les url de tous les livres de la catégorie.
def scrap_category(url_category):
    all_links = get_links_category(url_category)
    scrap_category_books(all_links)
    return all_links

# Etape 3 : Extraire tous les produits de toutes les catégories :
def etl_categories(home_url):
    url = home_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    categories_links = [url + link.get('href') for link in soup.select('div ul li a')[:-1]]

    for category_link in categories_links:
        scrap_category(category_link)

# Ce code s'éxécute seulement si je fais >>> python missionP2OC.py dans le terminal
if __name__ == "__main__":
    home_url = "https://books.toscrape.com/"
    etl_categories(home_url)

































