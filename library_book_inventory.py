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

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_publication_year(self):
        return self._publication_year
    
    def get_copies_available(self):
        return self._copies_available
    
    #def 