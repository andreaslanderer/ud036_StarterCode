import webbrowser

class Movie():
	def __init__ (self, title, posterUrl, trailerUrl):
		self.title = title
		self.posterUrl = posterUrl
		self.trailerUrl = trailerUrl

	def show_trailer(self):
		webbrowser.open(self.trailerUrl)


spider_man = Movie(title = "Spiderman", 
					posterUrl = "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
					trailerUrl = "https://youtu.be/TYMMOjBUPMM")
spider_man.show_trailer()