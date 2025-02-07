"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Mason Jennings
Date: 2-7-2025
"""

class LibraryBookInventory:
    def __init__(self, title, author, publication_year, copies_available = 0,
                 copies_checked_out = 0) -> None:
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._copies_available = copies_available
        self._copies_checked_out = copies_checked_out

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_publication_year(self):
        return self._publication_year

    def get_copies_available(self):
        return self._copies_available
    
    def get_copies_checked_out(self):
        return self._copies_checked_out

    def set_title(self, new_title):
        self._title = new_title
    
    def set_author(self, new_author):
        self._author = new_author

    def set_publication_year(self, new_publication_year):
        self._publication_year = new_publication_year

    def set_copies_available(self, new_copies_available):
        self._copies_available = new_copies_available

    def set_copies_checked_out(self, new_copies_checked_out):
        self._copies_checked_out = new_copies_checked_out

    def book_borrow(self):
        if self._copies_available > 0:
            self._copies_available -= 1
        else:
            print(f"Sorry, there are no copies of {self.get_title()} available.")

    def book_return(self):
        self._copies_available += 1
        print(f"{self.getTitle()} has been successfully returned.")