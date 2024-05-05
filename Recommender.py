# Authors: Ismail Gul and Endalkachew Bogale Gelaw
# Date: 05/XXXXXXX/2024
# Description: This program contains the Recommender class which is used to recommend movies, TV shows, and books.

# Import Python modules
import tkinter, csv, os
from tkinter import filedialog
import tkinter.messagebox as messagebox

# Import custom modules
from Book import Book
from Show import Show

# Define the Recommender class
class Recommender:
    # Constructor function
    def __init__(self):
        self.__books = {}
        self.__shows = {}
        self.__associations = {}

    def load_books(self):
        # Prompt the user to select a file
        file_path = filedialog.askopenfilename(title="Select Book File", initialdir=os.getcwd(), filetypes=[("CSV files", "*.csv")])

        # If user cancels or doesn't select a file, return without loading
        while not file_path:
            file_path = filedialog.askopenfilename(title="Select Book File", initialdir=os.getcwd(),
                                                   filetypes=[("CSV files", "*.csv")])

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
        file_path = filedialog.askopenfilename(title="Select Show File", initialdir=os.getcwd(), filetypes=[("CSV files", "*.csv")])

        # If user cancels or doesn't select a file, return without loading
        while not file_path:
            file_path = filedialog.askopenfilename(title="Select Show File", initialdir=os.getcwd(),
                                                   filetypes=[("CSV files", "*.csv")])

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
                    print(f"Error loading show: {err}")         # In the GUI but not in the console????????????????????????????

        # Close the file
        file.close()

    def load_associations(self):
        # Prompt the user to select a file

        file_path = ""

        # If user cancels or doesn't select a file, return without loading
        while not file_path:
            file_path = filedialog.askopenfilename(title="Select Association File", initialdir=os.getcwd(),
                                                   filetypes=[("CSV files", "*.csv")])

        # Open the file and read line by line
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    # Extract data from CSV row
                    show_id, book_id = row

                    # Create association from show_id to book_id
                    if show_id not in self.__associations:
                        self.__associations[show_id] = {book_id:1}
                    elif book_id not in self.__associations[show_id]:
                        self.__associations[show_id][book_id] = 1
                    else:
                        self.__associations[show_id][book_id] += 1

                    # Create association from book_id to show_id
                    if book_id not in self.__associations:
                        self.__associations[book_id] = {show_id:1}
                    elif show_id not in self.__associations[book_id]:
                        self.__associations[book_id][show_id] = 1
                    else:
                        self.__associations[book_id][show_id] += 1

                except Exception as err:
                    print(f"Error loading association: {err}")      # In the GUI but not in the console????????????????????????????

        # Close the file
        file.close()

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
            if show.get_show_type() == 'TV Show':
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
        number_of_movies = 0

        for show in self.__shows.values():
            if show.get_show_type() == 'Movie':
                number_of_movies += 1
                ratings[show.get_rating()] = ratings.get(show.get_rating(), 0) + 1
                durations.append(int(show.get_duration().replace(' min', '')))
                for director in show.get_directors().split('\\'):
                    if director:
                        directors[director] = directors.get(director, 0) + 1
                for actor in show.get_actors().split('\\'):
                    if actor:
                        actors[actor] = actors.get(actor, 0) + 1
                for genre in show.get_genres().split('\\'):
                    if genre:
                        genres[genre] = genres.get(genre, 0) + 1

        # Calculate the statistics
        rating_percentages = {}

        for rating, count in ratings.items():
            if rating == "":
                rating = "None"
            # Calculate the percentage
            percentage = count / number_of_movies * 100

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
                f"Most Frequent Genre: {most_common_genre}"), rating_percentages

    def get_tv_stats(self):
        ratings = {}
        seasons = []
        actors = {}
        genres = {}
        number_of_tv_shows = 0

        for show in self.__shows.values():
            if show.get_show_type() == 'TV Show':
                number_of_tv_shows += 1
                ratings[show.get_rating()] = ratings.get(show.get_rating(), 0) + 1
                seasons.append(int(show.get_duration().replace(' Seasons', '').replace(' Season', '')))
                for actor in show.get_actors().split('\\'):
                    if actor:
                        actors[actor] = actors.get(actor, 0) + 1
                for genre in show.get_genres().split('\\'):
                    if genre:
                        genres[genre] = genres.get(genre, 0) + 1

        # Calculate the statistics
        rating_percentages = {}

        for rating, count in ratings.items():
            if rating == "":
                rating = "None"
            # Calculate the percentage
            percentage = count / number_of_tv_shows * 100

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
                f"Most Frequent Genre: {most_common_genre}"), rating_percentages

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
            return  # Do nothing

        # How is it for more than one most common author or publisher       ?????????????????????????????

        return (f"Average page count: {average_pages:.2f} pages\n\n"
                f"Most Prolific Author: {most_common_author}\n\n"
                f"Most Prolific Publisher: {most_common_publisher}")

    # Method to search in books
    def search_books(self, title, author, publisher):
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
            elif title == book.get_title() and any(author == a for a in authors):
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

        #for book in self.__books.values():
          #  authors = book.get_authors().split("\\")
          #  if (not title or title in book.get_title()) and \
           #         (not author or author in authors) and \
           #         (not publisher or publisher in book.get_publisher()):
           #     matching_books.append(book)

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
        book_row = (f"{'Title':<{max_title_length}} {'Author':<{max_author_length}} "
                    f"{'Publisher':<{max_publisher_length}}\n")

        # Add title, author and publisher of reach results at bottom row
        for book in matching_books:
            book_row += (f"{book.get_title():<{max_title_length}} "
                         f"{book.get_authors():<{max_author_length}} "
                         f"{book.get_publisher():<{max_publisher_length}}\n")

        return book_row

    # Method to get recommendations
    def get_recommendations(self, type, title):
        book_recommendations = ""
        show_recommendations = ""

        if type == "Movie" or type == "TV Show":
            # Search through the shows dictionary and determine the id associated with that title
            show_id = None
            for key, value in self.__shows.items():
                if value.get_title() == title:
                    show_id = key
                    break
            
            # Unknown title
            if show_id is None:
                tkinter.messagebox.showwarning("No Recommendations", f'There are no recommendations for "{title}".')
                return "No results"

            # Using that movie or tv show id, determine all of the books associated with that id in the association dictionary
            if show_id in self.__associations:
                associated_books = self.__associations[show_id]
                for book_id, count in associated_books.items():
                    # Construct recommendation string for each book
                    book_info = (f"Title:\n"
                                f"{self.__books[book_id].get_title()}\n"
                                f"Authors:\n"
                                f"{self.__books[book_id].get_authors()}\n"
                                f"Average Rating:\n"
                                f"{self.__books[book_id].get_average_rating()}\n"
                                f"ISBN:\n"
                                f"{self.__books[book_id].get_isbn()}\n"
                                f"ISBN13:\n"
                                f"{self.__books[book_id].get_isbn13()}\n"
                                f"Language Code:\n"
                                f"{self.__books[book_id].get_language()}\n"
                                f"Pages:\n"
                                f"{self.__books[book_id].get_pages()}\n"
                                f"Rating Count:\n"
                                f"{self.__books[book_id].get_book_rating()}\n"
                                f"Publication Date:\n"
                                f"{self.__books[book_id].get_pub_date()}\n"
                                f"Publisher:\n"
                                f"{self.__books[book_id].get_publisher()}\n")
                    
                    book_recommendations += book_info

                return book_recommendations  # Moved the return outside the loop

        elif type == "Book":
            book_id = None
            for key, value in self.__books.items():
                if value.get_title() == title:
                    book_id = key
                    break
            
            if book_id is None:
                tkinter.messagebox.showwarning("No Recommendations", f'There are no recommendations for "{title}".')
                return "No results"

            if book_id in self.__associations:
                associated_shows = self.__associations[book_id]
                for show_id, count in associated_shows.items():

                    show_info = (f"Title:\n{self.__shows[show_id].get_title()}\n" +
                                (f"Directors:\n{self.__shows[show_id].get_directors()}\n" if self.__shows[show_id].get_directors() else "") +
                                (f"Actors:\n{self.__shows[show_id].get_actors()}\n" if self.__shows[show_id].get_actors() else "") + 
                                (f"Average Rating:\n{self.__shows[show_id].get_average_rating()}\n" if self.__shows[show_id].get_average_rating() else "") +
                                (f"Country:\n{self.__shows[show_id].get_country()}\n" if self.__shows[show_id].get_country() else "") + 
                                (f"Date Added:\n{self.__shows[show_id].get_date_added()}\n" if self.__shows[show_id].get_date_added() else "") + 
                                (f"Release Year:\n{self.__shows[show_id].get_release_year()}\n" if self.__shows[show_id].get_release_year() else "") + 
                                (f"Rating:\n{self.__shows[show_id].get_rating()}\n" if self.__shows[show_id].get_rating() else "") + 
                                (f"Duration:\n{self.__shows[show_id].get_duration()}\n" if self.__shows[show_id].get_duration() else "") + 
                                (f"Genres:\n{self.__shows[show_id].get_listed_in()}\n" if self.__shows[show_id].get_listed_in() else "") + 
                                (f"Description:\n{self.__shows[show_id].get_description()}\n" if self.__shows[show_id].get_description() else ""))
                    
                    show_recommendations += show_info

                return show_recommendations  # Moved the return outside the loop

        # Moved return "No results" outside the if-elif block
        tkinter.messagebox.showwarning("Invalid Type", f'Invalid media type: "{type}". Please choose "Movie", "TV Show", or "Book".')
        return "No results"

    def search_TV_Movies(self, show_type, show_title, show_director, show_actor, show_genre):
        show_type = show_type.strip()
        show_title = show_title.strip()
        show_director = show_director.strip()
        show_actor = show_actor.strip()
        show_genre = show_genre.strip()

        # If the show_type is neither 'Movie' nor 'TV Show'
        if show_type not in ["Movie", "TV Show"]:
            # Spawn a showerror messagebox
            tkinter.messagebox.showerror("Error", "Please select 'Movie' or 'TV Show' from Type first.")
            # Return the string 'No Results'
            return "Nothing is searched"

        # If the show_title, show_director, show_actor, and show_genre are all empty
        if not show_title and not show_director and not show_actor and not show_genre:
            # Spawn a showerror messagebox
            tkinter.messagebox.showerror("Error",
                                         "Please enter one or more of the Title, Director, Actor, and/or Genre first.")
            # Return the string 'No Results'
            return "Nothing is searched"

        # Otherwise, search through the dictionary of shows
        matching_shows = []
        for show in self.__shows.values():
            directors = show.get_directors().split("\\")
            actors = show.get_actors().split("\\")
            genres = show.get_genres().split("\\")
            if (not show_type or show_type == show.get_show_type()) and \
                    (not show_title or show_title in show.get_title()) and \
                    (not show_director or any(show_director in d for d in directors)) and \
                    (not show_actor or any(show_actor in a for a in actors)) and \
                    (not show_genre or any(show_genre in g for g in genres)):
                matching_shows.append(show)

        # If no results found
        if not matching_shows:
            return "Search can't find a matching results."

        # Find the maximum length of type, title, director, actor, and genre for pretty printing
        max_type_length = 0
        max_title_length = 0
        max_director_length = 0
        max_actor_length = 0
        max_genre_length = 0

        # Iterate over each show in the list
        for show in matching_shows:
            # Update the maximum lengths if the current show's type, title, director, actor, or genre is longer
            if len(show.get_show_type()) > max_type_length:
                max_type_length = len(show.get_show_type())
            if len(show.get_title()) > max_title_length:
                max_title_length = len(show.get_title())
            if len(show.get_directors()) > max_director_length:
                max_director_length = len(show.get_directors())
            if len(show.get_actors()) > max_actor_length:
                max_actor_length = len(show.get_actors())
            if len(show.get_genres()) > max_genre_length:
                max_genre_length = len(show.get_genres())

        # Header row
        show_row = (
            f"{'Type':<{max_type_length}} {'Title':<{max_title_length}} {'Director':<{max_director_length}} "
            f"{'Actor':<{max_actor_length}} {'Genre':<{max_genre_length}}\n")

        # Add type, title, director, actor, and genre of each result at bottom row
        for show in matching_shows:
            show_row += (f"{show.get_show_type():<{max_type_length}} {show.get_title():<{max_title_length}} "
                         f"{show.get_directors():<{max_director_length}} {show.get_actors():<{max_actor_length}} "
                         f"{show.get_genres():<{max_genre_length}}\n")

        return show_row

