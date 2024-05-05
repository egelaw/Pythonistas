# Authors: Ismail Gul and Endalkachew Bogale Gelaw
# Date: 04/29/2024
# Description: This program contains the Book class which is a subclass of the Media class.

# Import appropriate modules
from Media import Media

# Define the Book class
class Book(Media):
    """
    This class represents the Book class which is a subclass of the Media class.
    :param id: The unique identifier for the media item.
        :type id: int
    :param title: The title of the media item.
        :type title: str
    :param average_rating: The average rating of the media item.
        :type average_rating: float
    :param authors: The authors of the book.
        :type authors: str
    :param isbn: The ISBN of the book.
        :type isbn: str
    :param isbn13: The ISBN13 of the book.
        :type isbn13: str
    :param language: The language of the book.
        :type language: str
    :param pages: The number of pages in the book.
        :type pages: int
    :param book_rating: The rating of the book.
        :type book_rating: float
    :param pub_date: The publication date of the book.
        :type pub_date: str
    :param publisher: The publisher of the book.
        :type publisher: str
    :return: None
    """
    # Constructor function    
    def __init__(self, id, title, average_rating, authors, isbn, isbn13, language, pages, book_rating, pub_date, publisher):
        super().__init__(id, title, average_rating)
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__language = language
        self.__pages = pages
        self.__book_rating = book_rating
        self.__pub_date = pub_date
        self.__publisher = publisher

    # Add appropriate getter and setter functions
    def get_authors(self):
        return self.__authors
    
    def set_authors(self, authors):
        self.__authors = authors

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn13(self):
        return self.__isbn13

    def set_isbn13(self, isbn13):
        self.__isbn13 = isbn13

    def get_language(self):
        return self.__language

    def set_language(self, language):
        self.__language = language

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        self.__pages = pages

    def get_book_rating(self):
        return self.__book_rating

    def set_book_rating(self, book_rating):
        self.__book_rating = book_rating

    def get_pub_date(self):
        return self.__pub_date

    def set_pub_date(self, pub_date):
        self.__pub_date = pub_date

    def get_publisher(self):
        return self.__publisher
    
    def set_publisher(self, publisher):
        self.__publisher = publisher
