class Movie:
    
    _reviews = []

    def __init__(self, title):
        if len(title) <= 0:
            raise Exception("title must be at least one character")
        self.title = title

    def average_rating(self):
        return sum(list(map(lambda review: review.rating, self._reviews)))/len(self._reviews)

    @classmethod
    def highest_rated(cls):
        return Movie("Rashomon")

    def settitle(self, title):
        self._title = title

    def gettitle(self):
        return self._title

    title = property(gettitle, settitle)

    def add_review(self, review):
        Movie._reviews.append(review)

    def getreviewers(self):
        return list(map(lambda review: review.viewer, self._reviews))
    reviewers = property(getreviewers)
    
    def getreviews(self):
        return Movie._reviews
    reviews = property(getreviews)
    
    def reviewed_movies(self):
        return map(lambda review: review.movie, Movie._reviews)

