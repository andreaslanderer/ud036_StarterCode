""" This module contains the EntertainmentCenter class. """

from media import Movie
from fresh_tomatoes import open_movies_page

class EntertainmentCenter(object):

    """ This class contains two static methods: one method
    returns the list of movies and the other opens the
    browser in order to display the movies."""

    @staticmethod
    def get_movies():

        """ This method returns the list of movies to be
        displayed by the browser. """

        spider_man = Movie(
            title="Spiderman",
            posterUrl="https://goo.gl/5b1XVu",
            trailerUrl="https://youtu.be/TYMMOjBUPMM")

        pirates_of_the_caribbean = Movie(
            title="Pirates of the Caribbean",
            posterUrl="https://goo.gl/rVNEYW",
            trailerUrl="https://youtu.be/naQr0uTrH_s")

        a_beautiful_mind = Movie(
            title="A beautiful mind",
            posterUrl="https://goo.gl/kRzPR5",
            trailerUrl="https://youtu.be/aS_d0Ayjw4o")

        interstellar = Movie(
            title="Interstellar",
            posterUrl="https://goo.gl/zfIH18",
            trailerUrl="https://youtu.be/zSWdZVtXT7E")

        armageddon = Movie(
            title="Armageddon",
            posterUrl="https://goo.gl/2VTO2f",
            trailerUrl="https://youtu.be/kg_jH47u480")

        meet_joe_black = Movie(
            title="Meet Joe Black",
            posterUrl="https://goo.gl/JuWd4h",
            trailerUrl="https://youtu.be/_zIOjl93WrU")

        return [spider_man, pirates_of_the_caribbean, a_beautiful_mind,
                interstellar, armageddon, meet_joe_black]


    @staticmethod
    def play():

        """ This method opens the browser and displays the
        website. """

        movies = EntertainmentCenter.get_movies()
        open_movies_page(movies)
