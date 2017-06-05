from media import Movie
from fresh_tomatoes import open_movies_page

class EntertainmentCenter():

	def get_movies(self):
		spider_man = Movie(
			title = "Spiderman", 
			posterUrl = "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
			trailerUrl = "https://youtu.be/TYMMOjBUPMM")

		pirates_of_the_caribbean = Movie(
			title = "Pirates of the Caribbean",
			posterUrl = "https://i.jeded.com/i/pirates-of-the-caribbean-1-the-curse-of-the-black-pearl.12323.jpg",
			trailerUrl = "https://youtu.be/naQr0uTrH_s")

		a_beautiful_mind = Movie(
			title = "A beautiful mind",
			posterUrl = "http://www.impawards.com/2001/posters/beautiful_mind_xlg.jpg",
			trailerUrl = "https://youtu.be/aS_d0Ayjw4o")

		interstellar = Movie(
			title = "Interstellar",
			posterUrl = "https://www.mauvais-genres.com/19056-thickbox_default/interstellar-french-movie-poster-15x21-2014-christopher-nolan-matthew-mcconaughey.jpg",
			trailerUrl = "https://youtu.be/zSWdZVtXT7E")

		armageddon = Movie(
			title = "Armageddon",
			posterUrl = "https://s-media-cache-ak0.pinimg.com/originals/1f/d1/fb/1fd1fb6632e6641a4046a5daf94e483b.jpg",
			trailerUrl = "https://youtu.be/kg_jH47u480")

		meet_joe_black = Movie(
			title = "Meet Joe Black",
			posterUrl = "http://www.moviepostersuk.com/catalogue/images/catalogueusonesheets/meetjoeblack.jpg",
			trailerUrl = "https://youtu.be/_zIOjl93WrU")

		return [spider_man, pirates_of_the_caribbean, a_beautiful_mind, interstellar, armageddon, meet_joe_black]


	def play(self):
		movies = self.get_movies()
		open_movies_page(movies)