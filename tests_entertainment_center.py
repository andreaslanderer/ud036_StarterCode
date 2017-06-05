from unittest import TestCase
from unittest import main
from entertainment_center import EntertainmentCenter

class EntertainmentCenterTests(TestCase):

	def test_get_movies(self):
		# Arrange
		number_of_movies = 6

		# Act
		entertainment_center = EntertainmentCenter()

		# Assert
		self.assertEquals(number_of_movies, entertainment_center.get_movies().__len__())


if __name__ == '__main__':
	main()