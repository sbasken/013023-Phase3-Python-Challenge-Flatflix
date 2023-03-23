from .review import Review

class Viewer:

    usernames = []
    
    def __init__(self, username):
        self.username = username

        Viewer.usernames.append(self.username)

        self.reviews = []

    # username property goes here!
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if (username not in Viewer.usernames) and (6 <= len(username) <= 16):
            self._username = username
        else:
            raise Exception("Usernames must be unique strings between 6 and 16 characters!")

    def add_review(self, review):
        self.reviews.append(review)
        
    @property
    def reviewed_movies(self):
        return [ review.movie for review in self.reviews ]


    def reviewed_movie(self, movie):
        return [ review.movie for review in self.reviews if review.movie == movie]

    def rate_movie(self, movie, rating):
        if self.reviewed_movie(movie):
            for review in self.reviews:
                review.rating = rating
        else:
            Review(self, movie, rating)


