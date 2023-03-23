class Movie:

    all_movies = []
    
    def __init__(self, title):
        self.title = title

        self.reviews =[]
        Movie.all_movies.append(self)

    # title property goes here!
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception("titles must be strings greater than 0 characters!")
        
    def add_review(self, review):
        self.reviews.append(review)

    @property
    def reviewers(self):
        return [ review.viewer for review in self.reviews ]

    def average_rating(self):
        total = 0
        for review in self.reviews:
            total += review.rating
        return total / len(self.reviews)

    @classmethod
    def highest_rated(cls):
        highest_rating = 0
        found_movie = ""
        for movie in cls.all_movies:
            if movie.average_rating() > highest_rating:
                highest_rating = movie.average_rating()
                found_movie = movie
        return found_movie
