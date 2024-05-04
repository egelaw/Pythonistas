# Authors: Ismail Gul and Endalkachew Bogale Gelaw
# Date: 05/XXXXXXX/2024
# Description: This program contains the Recommender class which is used to recommend movies, TV shows, and books.

import csv, os
import tkinter
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

    def load_shows(self):
        # Prompt the user to select a file
        file_path = filedialog.askopenfilename(title="Select Show File", initialdir=os.getcwd(),
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
                    id, show_type, title, directors, cast, average_rating, country, date_added, release_year, rating, duration, listed_in, description = row

                    # Create Show object
                    show = Show(id, title, float(average_rating), show_type, directors, cast, country, date_added,
                                int(release_year), rating, duration, listed_in, description)

                    # Store Show object in __shows dictionary
                    self.__shows[id] = show

                except Exception as err:
                    print(f"Error loading show: {err}")

        # Close the file
        file.close()

    def load_associations(self):
        # Prompt the user to select a file
        file_path = filedialog.askopenfilename(title="Select Association File", initialdir=os.getcwd(),
                                               filetypes=[("CSV files", "*.csv")])

        # If user cancels or doesn't select a file, return without loading
        if not file_path:
            return

        # Open the file and read line by line
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    # Extract data from CSV row
                    id1, id2 = row

                    # Create association from id1 to id2
                    if id1 not in self.__associations:
                        self.__associations[id1] = {}
                    if id2 not in self.__associations[id1]:
                        self.__associations[id1][id2] = 1
                    else:
                        self.__associations[id1][id2] += 1

                    # Create association from id2 to id1
                    if id2 not in self.__associations:
                        self.__associations[id2] = {}
                    if id1 not in self.__associations[id2]:
                        self.__associations[id2][id1] = 1
                    else:
                        self.__associations[id2][id1] += 1

                except Exception as err:
                    print(f"Error loading association: {err}")

    def get_movie_list(self):
        # Find the maximum length of title and runtime for pretty printing
        movie_shows = []
        for show in self.__shows.values():
            if show.get_show_type() == 'Movie':
                movie_shows.append(show)

        if movie_shows:
            max_title_length = 0
            max_runtime_length = 0

            for show in movie_shows:
                title_length = len(show.get_title())
                runtime_length = len(show.get_duration())

                if title_length > max_title_length:
                    max_title_length = title_length
                if runtime_length > max_runtime_length:
                    max_runtime_length = runtime_length

            # Initialize the movie list with the header
            movie_list = f"{'Title':<{max_title_length}} {'Runtime':<{max_runtime_length}}\n"

            # Add the title and runtime of each movie to the movie list
            for show in movie_shows:
                movie_list += f"{show.get_title():<{max_title_length}} {show.get_duration():<{max_runtime_length}}\n"
        else:
            movie_list = "No movies found.\n"

        return movie_list

    def get_tv_list(self):
        tv_shows = []
        for show in self.__shows.values():
            if show.get_show_type() == 'Movie':
                tv_shows.append(show)

        if tv_shows:
            max_title_length = 0
            max_seasons_length = 0

            for show in tv_shows:
                title_length = len(show.get_title())
                seasons_length = len(show.get_duration())

                if title_length > max_title_length:
                    max_title_length = title_length
                if seasons_length > max_seasons_length:
                    max_seasons_length = seasons_length

            # Initialize the movie list with the header
            tv_show_list = f"{'Title':<{max_title_length}} {'Runtime':<{max_seasons_length}}\n"

            # Add the title and runtime of each movie to the movie list
            for show in tv_shows:
                tv_show_list += f"{show.get_title():<{max_title_length}} {show.get_duration():<{max_seasons_length}}\n"
        else:
            tv_show_list = "No TV shows found.\n"

        return tv_show_list

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

        # Header row
        book_row = f"{'Title':<{max_title_length}} {'Author(s)':<{max_authors_length}}\n"

        # Add the title and authors of each book at bottom row
        for book in self.__books.values():
            book_row += f"{book.get_title():<{max_title_length}} {book.get_authors():<{max_authors_length}}\n"

        return book_row

    def get_movie_stats(self):
        ratings = {}
        durations = []
        directors = {}
        actors = {}
        genres = {}

        for show in self.__shows.values():
            if show.get_show_type() == 'Movie':
                ratings[show.get_rating()] = ratings.get(show.get_rating(), 0) + 1
                durations.append(int(show.get_duration().replace(' min', '')))
                for director in show.get_directors().split(', '):
                    directors[director] = directors.get(director, 0) + 1
                for actor in show.get_actors().split(', '):
                    actors[actor] = actors.get(actor, 0) + 1
                for genre in show.get_genres().split(', '):
                    genres[genre] = genres.get(genre, 0) + 1

        # Calculate the statistics
        rating_percentages = {}

        for rating, count in ratings.items():
            # Calculate the percentage
            percentage = count / len(self.__shows) * 100

            # Add the rating and its percentage to the rating_percentages dictionary
            rating_percentages[rating] = percentage

        average_duration = sum(durations) / len(durations)
        most_common_director = max(directors, key=directors.get)
        most_common_actor = max(actors, key=actors.get)
        most_common_genre = max(genres, key=genres.get)

        ratings_str = ""
        for rating, percentage in rating_percentages.items():
            formatted_percentage = f"{percentage:.2f}%"
            ratings_str += f"{rating}: {formatted_percentage}\n"

        # Return the statistics as a formatted string
        return (f"Ratings: \n{ratings_str}\n\n"
                f"Average Movie Duration: {average_duration:.2f} minutes\n\n"
                f"Most Prolific Director: {most_common_director}\n\n"
                f"Most Prolific Actor: {most_common_actor}\n\n"
                f"Most Frequent Genre: {most_common_genre}")

    def get_tv_stats(self):
        ratings = {}
        seasons = []
        actors = {}
        genres = {}

        for show in self.__shows.values():
            if show.get_show_type() == 'TV Show':
                ratings[show.get_rating()] = ratings.get(show.get_rating(), 0) + 1
                seasons.append(int(show.get_duration().replace(' Seasons', '').replace(' Season', '')))
                for actor in show.get_actors().split(', '):
                    actors[actor] = actors.get(actor, 0) + 1
                for genre in show.get_genres().split(', '):
                    genres[genre] = genres.get(genre, 0) + 1

        # Calculate the statistics
        rating_percentages = {}

        for rating, count in ratings.items():
            # Calculate the percentage
            percentage = count / len(self.__shows) * 100

            # Add the rating and its percentage to the rating_percentages dictionary
            rating_percentages[rating] = percentage

        average_seasons = sum(seasons) / len(seasons)
        most_common_actor = max(actors, key=actors.get)
        most_common_genre = max(genres, key=genres.get)

        ratings_str = ""
        for rating, percentage in rating_percentages.items():
            formatted_percentage = f"{percentage:.2f}%"
            ratings_str += f"{rating}: {formatted_percentage}\n"

        # Return the statistics as a formatted string
        return (f"Ratings: \n{ratings_str}\n\n"
                f"Average Number of Seasons: {average_seasons:.2f}\n\n"
                f"AMost Prolific Actor: {most_common_actor}\n\n"
                f"Most Frequent Genre: {most_common_genre}")

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
        try:
            average_pages = sum(pages) / len(pages)
            most_common_author = max(authors, key=authors.get)
            most_common_publisher = max(publishers, key=publishers.get)
        except ZeroDivisionError:
            return # Do nothing 

        # How is it for more than one most common author or publisher       ?????????????????????????????

        return (f"Average page count: {average_pages:.2f} pages\n\n"
                f"Most Prolific Author: {most_common_author}\n\n"
                f"Most Prolific Publisher: {most_common_publisher}")

    # Method to search in books
    def search_books(self, title="", author="", publisher=""):
        title = title.strip()
        author = author.strip()
        publisher = publisher.strip()

        # If the title, author, and publisher are all empty
        if not title and not author and not publisher:
            # Spawn a showerror messagebox
            tkinter.messagebox.showerror("Error", "Please enter one or more of Title, Author, or Publisher.")
            # Return the string 'No Results'
            return "Nothing is searched"

        # Otherwise, search through the dictionary of books
        matching_books = []
        for book in self.__books.values():
            authors = book.get_authors().split("\\")
            if title == book.get_title() and any(author == a for a in authors) and publisher == book.get_publisher():
                matching_books.append(book)
            elif title == book.get_title() and author == book.get_authors() and publisher == book.get_publisher():
                matching_books.append(book)
            elif title == book.get_title() and publisher == book.get_publisher():
                matching_books.append(book)
            elif any(author == a for a in authors) and publisher == book.get_publisher():
                matching_books.append(book)
            elif title == book.get_title():
                matching_books.append(book)
            elif any(author == a for a in authors):
                matching_books.append(book)
            elif publisher == book.get_publisher():
                matching_books.append(book)

        # If no results found
        if not matching_books:
            return "Search can't find a matching results."

        # Find the maximum length of title, author, and publisher for pretty printing
        max_title_length = 0
        max_author_length = 0
        max_publisher_length = 0

        # Iterate over each book in the list
        for book in matching_books:
            # Update the maximum lengths
            if len(book.get_title()) > max_title_length:
                max_title_length = len(book.get_title())
            if len(book.get_authors()) > max_author_length:
                max_author_length = len(book.get_authors())
            if len(book.get_publisher()) > max_publisher_length:
                max_publisher_length = len(book.get_publisher())

        # Header row
        book_row = (f"{'Title':<{max_title_length}}   {'Author':<{max_author_length}}   "
                    f"{'Publisher':<{max_publisher_length}}\n")
        
        # Add title, author and publisher of rearch results at bottom row
        for book in matching_books:
            book_row += (f"{book.get_title():<{max_title_length}}   "
                         f"{book.get_authors():<{max_author_length}}   "
                         f"{book.get_publisher():<{max_publisher_length}}\n")

        return book_row