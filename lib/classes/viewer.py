from .review import Review

class Viewer:
    
    all = []

    def __init__(self, username):
        self.username = username
        Viewer.all.append(self)
        self._reviews = []

    def setusername(self, username):        
        if username in [viewer.username for viewer in Viewer.all]:
            raise Exception("usernames must be unique")
        if not 6 <= len(username) <= 16:
            raise Exception("usernames must be 6 to 16 characters") 
        self._username = username

    def getusername(self):
        return self._username
    username = property(getusername, setusername)

    def add_review(self, review):
        self._reviews.append(review)

    def getreviews(self):
        return self._reviews
    reviews = property(getreviews)

    def get_reviewed_movies(self):
        return [review.movie for review in self._reviews]
    reviewed_movies = property(get_reviewed_movies)

    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies

    def rate_movie(self, movie, rating):
        if not self.reviewed_movie(movie):
            print(f"haven't reviewed yet: {movie.title}")
            Review(self, movie, rating)
        else:
            print(f"reviewing: {movie.title}")
            [r for r in self._reviews if r.movie == movie][0].rating = rating

