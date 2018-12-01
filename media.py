import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(
        self, movieTitle, movieStoryline, posterImage,
        trailerYoutube, duration, genre
    ):
        self.title = movieTitle
        self.storyline = movieStoryline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYoutube
        self.duration = duration
        self.genre = genre
