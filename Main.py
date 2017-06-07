""" This module starts the entertainment center. """

from entertainment_center import EntertainmentCenter
from media import Movie

SPIDER_MAN = Movie(
    title="Spiderman",
    posterUrl="https://goo.gl/5b1XVu",
    trailerUrl="https://youtu.be/TYMMOjBUPMM")

PIRATES_OF_THE_CARIBBEAN = Movie(
    title="Pirates of the Caribbean",
    posterUrl="https://goo.gl/rVNEYW",
    trailerUrl="https://youtu.be/naQr0uTrH_s")

A_BEAUTIFUL_MIND = Movie(
    title="A beautiful mind",
    posterUrl="https://goo.gl/kRzPR5",
    trailerUrl="https://youtu.be/aS_d0Ayjw4o")

INTERSTELLAR = Movie(
    title="Interstellar",
    posterUrl="https://goo.gl/zfIH18",
    trailerUrl="https://youtu.be/zSWdZVtXT7E")

ARMAGEDDON = Movie(
    title="Armageddon",
    posterUrl="http://bit.ly/2qU7cA9",
    trailerUrl="https://youtu.be/kg_jH47u480")

MEET_JOE_BLACK = Movie(
    title="Meet Joe Black",
    posterUrl="https://goo.gl/JuWd4h",
    trailerUrl="https://youtu.be/_zIOjl93WrU")

MOVIE_LIST = [SPIDER_MAN, PIRATES_OF_THE_CARIBBEAN, A_BEAUTIFUL_MIND,
              INTERSTELLAR, ARMAGEDDON, MEET_JOE_BLACK]

CENTER = EntertainmentCenter(MOVIE_LIST)
CENTER.play()
