## Projet : Utilisez les bases de Python pour l'analyse de marché
### Tables des matières :
1. Description générale du projet.
2. Configurations compatibles.
3. Installation du programme.
4. Fonctionnalités.
5. Démarrage du programme.

## 1. Descripton générale du projet :

Ce projet a été réalisé dans le cadre de la formation de
développeur Python proposée par OpenClassrooms. Le thème principal étant
la gestion des données à l'aide du processus ETL (extract-transform-load),
l'objectif de ce projet est de mettre en place un programme (un scraper)
développé en Python, capable d'extraire un certain nombre
de données(prix,catégorie,...) à partir d'une librairie
en ligne [Books to Scrape](https://books.toscrape.com/).
Les informations extraites serviront notamment à une analyse marketing.

## 2. Configurations compatibles :

* Python 3.10.7
* Windows 10
* Mac
* Linux

## 3. Installation du programme :
Ce programme utilise les librairies Python suivantes :

beautifulsoup4 4.11.1\
bs4 0.0.1\
certifi 2022.9.24\
charset-normalizer 2.1.1\
html5lib 1.1\
idna 3.4\
lxml 4.9.1\
python-slugify 6.1.2\
requests 2.28.1
six 1.16.0\
soupsieve 2.3.2.post1\
text-unidecode 1.3\
urllib3 1.26.12\
webencodings 0.5.1

## 4. Fonctionnalités :

* <u> Fonctionnalité 1</u> : Scrapper la page d'un <b>livre</b> avec la fonction
  **scrap_book(url)**. Ici url est l'url d'un livre.
* <u> Fonctionnalité 2</u> : Scrapper la page d'une <b>catégorie</b> avec la fonction
  **scrap_category(url)**. Ici url est l'url d'une catégorie.
* <u> Fonctionnalité 3</u> : Scrapper <b>tout le site</b> avec la fonction **etl_categories(url)**. Ici url est l'url du site <a>https://books.toscrape.com/</a>.

## 5. Démarrage du programme :

1. Ouvrir un terminal (ex: Cygwin pour Windows, le terminal pour Mac) ou dans un IDE (ex: PyCharm).
2. Télécharger le dossier contenant le projet puis se placer dans ce dossier sur le terminal.
3. Créer un environnement virtuel avec :
  > $<b> python -m venv <nom de l'environnement></b> 
4. Activer l'environnement virtuel en éxécutant :
  > $ <b>source env/bin/activate</b>  (sur Mac) 

  > $ <b>env/Scripts/activate.bat</b> (sur Windows)
5. Installer les paquets présents dans le fichier (ce fichier se trouve dans le dossier du projet avec main.py) requirements.txt avec :
  > $ <b>pip install -r requirements.txt</b> 
6. Finalement, lancer le script avec
> $ <b>python main.py</b> 


---




