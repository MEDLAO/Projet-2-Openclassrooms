from scrap_book import scrap_book
from scrap_category import scrap_category
from scrap_all_categories import etl_categories

print("Welcome to Books to Scrap Scrapping !")

while True:

    print("Choose an option :")
    print("1- Scrap a book ")
    print("2- Scrap a category ")
    print("3- Scrap the whole website ")
    print("4- Exit")

    option = int(input())

    if option == 1:
        print("Please provide the url of the book:")
        url = str(input())
        scrap_book(url)
        print("You will find info of the book in the folder all_books.")

    elif option == 2:
        print("Please provide the url of the category:")
        url = str(input())
        scrap_category(url)
        print("You will find info of all category books in the folder all_books")

    elif option == 3:
        print("Please provide the url of Books to scrap:")
        url = str(input())
        etl_categories(url)
        print("You will find info of all website books in the folder all_books")

    elif option == 4:
        print("Thank you !")
        break

    else:
        print("Please choose a number between 1 and 4.")


