# Authors: Ismail Gul and Endalkachew Bogale Gelaw
# Date: 05/XXXXXXX/2024
# Description: This program contains the Recommender class which is used to recommend movies, TV shows, and books.

import csv, os
from tkinter import filedialog
import tkinter.messagebox as messagebox

from Book import Book
from Show import Show


# Define the Recommender class
class Recommender:
    # Constructor function
    def __init__(self):
        self.__books = {}  # Key: book id, Value: Book object
        self.__shows = {}  # Key: show id, Value: Show object
        self.__associations = {}  # Key: book/show ID_outer, Value: Dictionary (Key: book/show ID_inner, Value: the no of times ID_outer and ID_inner are associated)

    def load_books(self):
        # Prompt the user to select a file
        file_path = filedialog.askopenfilename(title="Select Book File", initialdir=os.getcwd(),
                                               filetypes=[("CSV files", "*.csv")])

        # If user cancels or doesn't select a file, return without loading
        if not file_path:
            return

        # Open the file and read line by line
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                try:
                    # Extract data from CSV row
                    id, title, authors, average_rating, isbn, isbn13, language, pages, book_rating, pub_date, publisher = row

                    # Create Book object
                    book = Book(id, title, float(average_rating), authors, isbn, isbn13, language, int(pages),
                                int(book_rating), pub_date, publisher)

                    # Store Book object in _books dictionary
                    self.__books[id] = book
                except Exception as err:
                    print(f"Error loading book: {err}")  # In the GUI but not in the console???????

        # Close the file
        file.close()

    def get_book_list(self):
        # Check if there are any books in the __books dictionary
        if not self.__books:
            return

        max_title_length = 0
        max_authors_length = 0

        # Find the maximum length of title and authors
        for book in self.__books.values():
            title_length = len(book.get_title())
            authors_length = len(book.get_authors())

            if title_length > max_title_length:
                max_title_length = title_length
            if authors_length > max_authors_length:
                max_authors_length = authors_length

        # Initialize the book list with the header
        book_list = f"{'Title':<{max_title_length}} {'Author(s)':<{max_authors_length}}\n"

        # Add the title and authors of each book to the book list
        for book in self.__books.values():
            book_list += f"{book.get_title():<{max_title_length}} {book.get_authors():<{max_authors_length}}\n"

        return book_list

    def get_book_stats(self):
        pages = []
        authors = {}
        publishers = {}

        for book in self.__books.values():
            pages.append(int(book.get_pages()))
            for author in book.get_authors().split("\\"):
                authors[author] = authors.get(author, 0) + 1
            publishers[book.get_publisher()] = publishers.get(book.get_publisher(), 0) + 1

        # Calculate the statistics
        average_pages = sum(pages) / len(pages)
        most_common_author = max(authors, key=authors.get)
        most_common_publisher = max(publishers, key=publishers.get)

        # How is it for more than one most common author or publisher       ?????????????????????????????????????

        return (f"Average page count: {average_pages:.2f}\n\n"
                f"Most Prolific Author: {most_common_author}\n\n"
                f"Most Prolific Publisher: {most_common_publisher}")

    def load_shows(self):
        pass

    def load_associations(self):
        pass
