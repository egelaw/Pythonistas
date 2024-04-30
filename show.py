# Authors: Ismail Gul and Endalkachew Bogale Gelaw
# Date: 05/XXXXXXX/2024
# Description: This program contains the Show class which is a subclass of the Media class.

# Import appropriate modules
from media import Media

# Define the Show class
class Show(Media):
    """
    This class represents the Show class which is a subclass of the Media class.
    :param id: The unique identifier for the media item.
        :type id: int
    :param title: The title of the media item.
        :type title: str
    :param average_rating: The average rating of the media item.
        :type average_rating: float
    :param show_type: The type of the show.
        :type show_type: str
    :param directors: The directors of the show.
        :type directors: str
    :param actors: The actors in the show.
        :type actors: str
    :param country: The country where the show was produced.
        :type country: str
    :param date_added: The date the show was added.
        :type date_added: str
    :param release_year: The release year of the show.
        :type release_year: int
    :param rating: The rating of the show.
        :type rating: str
    :param duration: The duration of the show.
        :type duration: str
    :param genres: The genres of the show.
        :type genres: str
    :param description: The description of the show.
        :type description: str
    :return: None
    """
    # Constructor function
    def __init__(self, id, title, average_rating, show_type, directors, actors, country, date_added, release_year, rating, duration, genres, description):
        super().__init__(id, title, average_rating)
        self.__show_type = show_type
        self.__directors = directors
        self.__actors = actors
        self.__country = country
        self.__date_added = date_added
        self.__release_year = release_year
        self.__rating = rating  # Is this going to overwride the average_rating?
        self.__duration = duration
        self.__genres = genres
        self.__description = description
    
    # Add appropriate getter and setter functions
    def get_show_type(self):
        return self.__show_type
    
    def set_show_type(self, show_type):
        self.__show_type = show_type

    def get_directors(self):
        return self.__directors
    
    def set_directors(self, directors):
        self.__directors = directors

    def get_actors(self):
        return self.__actors
    
    def set_actors(self, actors):
        self.__actors = actors

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_date_added(self):
        return self.__date_added
    
    def set_date_added(self, date_added):
        self.__date_added = date_added

    def get_release_year(self):
        return self.__release_year
    
    def set_release_year(self, release_year):
        self.__release_year = release_year

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_duration(self):
        return self.__duration
    
    def set_duration(self, duration):
        self.__duration = duration

    def get_genres(self):
        return self.__genres
    
    def set_genres(self, genres):
        self.__genres = genres

    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description
