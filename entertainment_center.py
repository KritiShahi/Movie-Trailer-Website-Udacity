"""Two files media.py and fresh_tomatoes.py are imported"""
import media
import fresh_tomatoes

"""Instances of class movie is being created i.e toy_story,avatar,
ki_and_ka,half_girlfriend,kapoor_and_sons,ek_tha_tiger"""
"""Values of movie_title,movie_story_line,
poster_image and trailer_youtube are passed as arguments"""

toy_story = media.Movie(
    "Toy Story", "Toys come to life",
    "http://c1.thejournal.ie/media/2014/11/toystory-2-390x285.jpg",
    "https://www.youtube.com/watch?v=rNk1Wi8SvNc"
    )

avatar = media.Movie(
    "Avatar", "A marine comes to an alien planet",
    "https://www.licenseindia.com/wp-content/uploads/2016/07/avatar.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
    )

ki_and_ka = media.Movie(
    "Ki and Ka", "story of a married couple",
    "http://s1.dmcdn.net/k-rZz/x240-eLz.jpg",
    "https://www.youtube.com/watch?v=B2fxtycjf_I"
    )

half_girlfriend = media.Movie(
    "Half Girlfriend", "Story of a girl who falls in love with boy",
    "http://www.lyricsmint.com/wp-content/uploads/2017/04/half-girlfriend.jpg",
    "https://www.youtube.com/watch?v=KmlBnmyelHI"
    )

kapoor_and_sons = media.Movie(
    "Kapoor and Sons", "Story about family",
    "https://c.tribune.com.pk/2016/03/1068783-main-1458381060-733-640x480.jpg",
    "https://www.youtube.com/watch?v=s7YYt9_KfsM"
    )

ek_tha_tiger = media.Movie(
    "Ek tha Tiger", "Story about the love for the country",
    "https://i.ytimg.com/vi/iKALdtWpHmg/movieposter.jpg",
    "https://www.youtube.com/watch?v=ePO5M5DE01I"
    )

"""The variable movies is list of instances created through class movie"""
movies = [
    toy_story, avatar,
    ki_and_ka, half_girlfriend,
    kapoor_and_sons, ek_tha_tiger
    ]

"""The file fresh_tomatoes.py has a function open_movies_page defined"""
"""The variable movies is passed as an argument"""
"""This opens the website contaning the list of movies defined as instances"""
fresh_tomatoes.open_movies_page(movies)
