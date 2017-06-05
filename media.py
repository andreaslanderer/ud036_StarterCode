import webbrowser

class Movie():
	def __init__ (self, title, posterUrl, trailerUrl):
		self.title = title
		self.poster_image_url = posterUrl
		self.trailer_youtube_url = trailerUrl

	def show_trailer(self):
		webbrowser.open(self.trailerUrl)