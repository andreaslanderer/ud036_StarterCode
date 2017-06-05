from unittest import TestCase
from unittest import main
from media import Movie

class MediaTests(TestCase):

	def test_init_movie_object(self):
		# Arrange
		title = "Rogue One - A Star Wars Story"
		url_to_poster = "http://t3.gstatic.com/images?q=tbn:ANd9GcSbnJ4Sbu-qCi93fXHwnF2T8SS2UgV8IHPtoyN7T4d-2bzjDYE0"
		url_to_trailer = "https://youtu.be/frdj1zb9sMY"

		# Act
		rogueOne = Movie(title = title, posterUrl = url_to_poster, trailerUrl = url_to_trailer)

		#Assert
		self.assertEqual(rogueOne.title, title)
		self.assertEqual(rogueOne.posterUrl, url_to_poster)
		self.assertEqual(rogueOne.trailerUrl, url_to_trailer)

if __name__ == '__main__':
	main()