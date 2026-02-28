import json

FILE_NAME = "library/books.json"


def load_library():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_library(library):
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)


def add_book(title, author, isbn):
    library = load_library()
    if isbn in library:
        print("Book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "available": True
        }
        save_library(library)
        print("Book added successfully.")


def display_books():
    library = load_library()
    if not library:
        print("No books available.")
    for isbn, book in library.items():
        status = "Available" if book["available"] else "Borrowed"
        print(f'{book["title"]} by {book["author"]} (ISBN: {isbn}) - {status}')


def search_book(keyword):
    library = load_library()
    found = False
    for isbn, book in library.items():
        if keyword.lower() in book["title"].lower():
            print(f'{book["title"]} by {book["author"]} (ISBN: {isbn})')
            found = True
    if not found:
        print("Book not found.")


def delete_book(isbn):
    library = load_library()
    if isbn in library:
        del library[isbn]
        save_library(library)
        print("Book deleted.")
    else:
        print("Book not found.")


def borrow_book(isbn):
    library = load_library()
    if isbn in library and library[isbn]["available"]:
        library[isbn]["available"] = False
        save_library(library)
        print("Book borrowed.")
    else:
        print("Book not available.")


def return_book(isbn):
    library = load_library()
    if isbn in library:
        library[isbn]["available"] = True
        save_library(library)
        print("Book returned.")
    else:
        print("Book not found.")