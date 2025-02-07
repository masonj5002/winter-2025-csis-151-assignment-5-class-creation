"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Mason Jennings
Date: 2-7-2025

Description:
    This class file contains a system to determine a library book's
        inventory: containing information about the book and the
        status of each of it's copies.
"""


class LibraryBookInventory:
    def __init__(
        self, title, author, publication_year, copies_available=0, copies_checked_out=0
    ) -> None:
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._copies_available = copies_available
        self._copies_checked_out = copies_checked_out

    """Returns the book's title"""
    def get_title(self):
        return self._title

    """Returns the book's author"""
    def get_author(self):
        return self._author

    """Returns the book's publication year"""
    def get_publication_year(self):
        return self._publication_year

    """Returns the number of copies available"""
    def get_copies_available(self):
        return self._copies_available

    """Returns the number of copies checked out"""
    def get_copies_checked_out(self):
        return self._copies_checked_out

    """Modifies the book's title"""
    def set_title(self, new_title):
        self._title = new_title

    """Modifies the book's author from parameter"""
    def set_author(self, new_author):
        self._author = new_author

    """Modifies the book's publication year from parameter"""
    def set_publication_year(self, new_publication_year):
        self._publication_year = new_publication_year

    """Modifies the number of copies available from parameter"""
    def set_copies_available(self, new_copies_available):
        self._copies_available = new_copies_available

    """Modifies the number of copies checked out from parameter"""
    def set_copies_checked_out(self, new_copies_checked_out):
        self._copies_checked_out = new_copies_checked_out

    """Checks out a copy from inventory"""
    def book_borrow(self):
        if self._copies_available > 0:
            self._copies_available -= 1
            self._copies_checked_out += 1
        else:
            print(f"Sorry, there are no copies of {self.get_title()} available.")

    """Checks in a copy from inventory"""
    def book_return(self):
        if self._copies_checked_out > 0:
            self._copies_available += 1
            self._copies_checked_out -= 1
            print(f"{self.get_title()} has been successfully returned.")
        else:
            print(
                f"{self.get_title()} cannot be returned because all copies are already checked in!"
            )
