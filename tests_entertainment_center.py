from unittest import TestCase
from unittest import main
from entertainment_center import EntertainmentCenter
from media import Movie

class EntertainmentCenterTests(TestCase):

    def test_get_movies(self):

        # Arrange
        number_of_movies = 1
        meet_joe_black = Movie(
            title="Meet Joe Black",
            posterUrl="https://goo.gl/JuWd4h",
            trailerUrl="https://youtu.be/_zIOjl93WrU")
        movie_list = [meet_joe_black]

        # Act
        center = EntertainmentCenter(movie_list)

        # Assert
        self.assertEquals(number_of_movies, len(center.movies))


if __name__ == '__main__':
    main()