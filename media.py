"""The module webbrowser is imported"""
import webbrowser


class Movie():
    """The class Movie helps to store movie related information

    Attributes:
        title: The title of the movie
        story_line: The description of movie in short
        poster_image_url: The URL address of the movie
        trailer_youtube_url: The URL address of trailer of the movie
    """

    def __init__(self, movie_title, movie_story_line, poster_image, trailer):
        """The init function is used to initialize the arguments passed"""
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """The show_trailer function opens the movie trailer in webbrowser"""
        webbrowser.open(self.trailer_youtube_url)







