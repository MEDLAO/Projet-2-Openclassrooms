from scrap_book import scrap_book
from scrap_category import scrap_category
from scrap_all_categories import etl_categories

# Le site dont sont extraites les informations est "Books to Scrape", son url est https://books.toscrape.com/
# Les informations extraites pour chaque livre sont :

# product_page_url
# universal_ product_code (upc)
# title
# price_including_tax
# price_excluding_tax
# number_available
# product_description
# category
# review_rating
# image_url

# Pour extraire les informations concernant un livre choisi et les charger dans un fichier csv, utiliser la fonction scrap_book(url).

# Pour extraire les informations de tous les livres d'une catégorie choisie, les charger dans un fichier csv et télécharger les images des livres, utiliser la fonction scrap_category(url).

# Pour faire de même que la fonction précédente pour toutes les catégories du site, utiliser la fonction etl_categories(url).

# Choisir l'une des trois fonctions et remplacer fonction(url) par le nom de la fonction à la ligne 29
# et mettre l'url(d'un livre, d'une catégorie ou du site) correspondant entre "" à la ligne 28 :

if __name__== "__main__":
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    scrap_book(url)

# Puis lancer dans le terminal python main.py

