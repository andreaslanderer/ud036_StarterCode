""" This module contains the EntertainmentCenter class. """

from fresh_tomatoes import open_movies_page


class EntertainmentCenter(object):

    """ This class contains two static methods: one method
    returns the list of movies and the other opens the
    browser in order to display the movies."""

    def __init__(self, movies):
        self.__movies = movies

    @property
    def movies(self):

        """ Get the list of movies """

        return self.__movies

    @movies.setter
    def movies(self, movies):

        """ Set the list of movies """

        self.__movies = movies

    def play(self):

        """ This method opens the browser and displays the
        website. """

        open_movies_page(self.__movies)
