import webbrowser

class Movie():
    VALID_RATINGS = ["A", "B", "C", "D"]
    TOTAL_RATING = "5"
    
    def __init__(self,movie_title, movie_story_line, poster_image, trailer_youtube, rating, categories):
        #constructor for Movie , assigning the instance variables the value
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.categories = categories
        
    def show_trailer(self):
        #opens the trailer in a browser
        webbrowser.open(self.trailer_youtube_url)
