# Movie class code is given in this lecture: https://classroom.udacity.com/nanodegrees/nd004/parts/0041345401/modules/356120945175460/lessons/997889780/concepts/10136290690923#
class Movie():
    '''The movie class makes movie objects that store a title, 
       poster image url, and a trailer url for youtube-hosted trailers'''

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
