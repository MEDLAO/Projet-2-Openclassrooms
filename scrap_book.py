import csv
import re
import os
from bs4 import BeautifulSoup
import requests
from slugify import slugify


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
    path_category = "all_books/" + donnees["category"]
    os.makedirs(path_category, exist_ok=True)
    book_csv = path_category + "/" + slugify(donnees["title"]) + ".csv"

    with open(book_csv, 'w', encoding="utf-8-sig") as fichier_csv:
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


if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    scrap_book(url, load=True)




































