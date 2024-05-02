# Authors: Ismail Gul and Endalkachew Bogale Gelaw
# Date: 04/28/2024
# Description: This program contains the Media class which is the base class for all media types.

# Define the Media class
class Media:
    """
    This class represents the base class for all media types.
    :param id: The unique identifier for the media item.
        :type id: int
    :param title: The title of the media item.
        :type title: str
    :param average_rating: The average rating of the media item.
        :type average_rating: float
    :return: None
    """
    # Constructor function
    def __init__(self, id, title, average_rating):
        self._id = id
        self._title = title
        self._average_rating = average_rating

    # Getter and setter functions
    def get_id(self):       # No setter for id because it should not be changed???
        return self._id
    
    def get_title(self):    # No setter for title because it should not be changed???
        return self._title
    
    def get_average_rating(self):
        return self._average_rating
    
    def set_average_rating(self, average_rating):
        self._average_rating = average_rating
