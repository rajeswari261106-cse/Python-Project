# q2_library_system.py

# Function to add books
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


# Function to borrow book
def borrow_book(catalog, borrowed_books, book_id):

    if book_id in catalog:

        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book {book_id} borrowed successfully")

        else:
            print("Book already borrowed")

    else:
        print("Book does not exist")


# Function to return book
def return_book(borrowed_books, book_id):

    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully")

    else:
        print("Book was not borrowed")


# Function to register members
def register_member(members, member_id):
    members.add(member_id)


# Function to show available books
def show_available(catalog, borrowed_books):

    print("\nAvailable Books:")

    for book_id, details in catalog.items():

        if book_id not in borrowed_books:

            title, author, year = details

            print(f"""
Book ID : {book_id}
Title   : {title}
Author  : {author}
Year    : {year}
""")


# Main Function
def main():

    # Dictionary
    catalog = {}

    # List
    borrowed_books = []

    # Set
    members = set()

    # Add 4 books
    add_book(catalog, 1, "Python Basics", "John Smith", 2020)
    add_book(catalog, 2, "Data Science", "Alice Brown", 2021)
    add_book(catalog, 3, "AI Fundamentals", "David Lee", 2022)
    add_book(catalog, 4, "Machine Learning", "Emma Wilson", 2023)

    # Register members
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)

    # Duplicate member
    register_member(members, 101)

    print("Registered Members:", members)

    # Borrow books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 2)

    # Return one book
    return_book(borrowed_books, 1)

    # Show available books
    show_available(catalog, borrowed_books)


# Run program
main()