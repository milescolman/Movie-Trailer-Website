

class Movie():
    '''The movie class makes movie objects that store a title, 
       poster image url, and a trailer url for youtube-hosted trailers'''

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
