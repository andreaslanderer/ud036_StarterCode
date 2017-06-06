""" This module contains the Movie class. """

import webbrowser

class Movie(object):

    """ This class contains all information regarding movies that
    are to be displayed on the movie website. Each movie consists
    of a title, a poster URL and a trailer URL. """

    def __init__(self, title, posterUrl, trailerUrl):
        self.title = title
        self.poster_image_url = posterUrl
        self.trailer_youtube_url = trailerUrl

    def show_trailer(self):

        """ This method opens a new window in a browser and navigates
        to the trailer URL. """

        webbrowser.open(self.trailer_youtube_url)
