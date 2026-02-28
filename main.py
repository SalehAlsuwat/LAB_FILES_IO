from library import librarian

while True:
    print("""
1. Add Book
2. Display Books
3. Search Book
4. Delete Book
5. Borrow Book
6. Return Book
7. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        librarian.add_book(title, author, isbn)

    elif choice == "2":
        librarian.display_books()

    elif choice == "3":
        keyword = input("Enter book title keyword: ")
        librarian.search_book(keyword)

    elif choice == "4":
        isbn = input("Enter ISBN: ")
        librarian.delete_book(isbn)

    elif choice == "5":
        isbn = input("Enter ISBN: ")
        librarian.borrow_book(isbn)

    elif choice == "6":
        isbn = input("Enter ISBN: ")
        librarian.return_book(isbn)

    elif choice == "7":
        print("Thank you for using the Library System.")
        break

    else:
        print("Invalid choice.")