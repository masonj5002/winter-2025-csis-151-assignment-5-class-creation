"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Mason Jennings
Date: 2-7-2025
"""
from library_book_inventory import LibraryBookInventory

def main():
    print("Hello world!")
    HPb1 = LibraryBookInventory("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 3)

    print(f"This book is called: {HPb1.get_title}.")
    print("More information")
    print(HPb1.get_author())
    print(HPb1.get_publication_year())
    print(HPb1.get_copies_available())
    print(HPb1.get_copies_checked_out())
    print(f"There are {HPb1.get_copies_available()} copies available.")
    print("Checking out four copies...")
    for copy in range(4):
        HPb1.book_borrow()
    print(f"There are {HPb1.get_copies_available()} copies available.")
    print(f"There are {HPb1.get_copies_checked_out()} copies checked out.")

    print("\nChanging Book Information...")
    HPb1.set_title("stony stony")
    HPb1.set_author("Roise Jennings")
    HPb1.set_publication_year("2025")
    HPb1.set_copies_available(16)
    HPb1.set_copies_checked_out(1)

    print("Outputting book information:")
    print(HPb1.get_title())
    print(HPb1.get_author())
    print(HPb1.get_publication_year())
    print(HPb1.get_copies_available())
    print(HPb1.get_copies_checked_out())
    print(f"There are {HPb1.get_copies_available()} copies available.")
    print("Checking out four copies...")
    for copy in range(4):
        HPb1.book_borrow()
    print(f"There are {HPb1.get_copies_available()} copies available.")
    print(f"There are {HPb1.get_copies_checked_out()} copies checked out.")
    print(f"Returning a copy...")
    HPb1.book_return()
    print(f"There are {HPb1.get_copies_available()} copies available.")
    print(f"There are {HPb1.get_copies_checked_out()} copies checked out.")

    print("returning five copies...")
    for copy in range(5):
        HPb1.book_return()
    print(f"There are {HPb1.get_copies_available()} copies available.")
    print(f"There are {HPb1.get_copies_checked_out()} copies checked out.")


if __name__ == "__main__":
    main()