class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        viewer.add_review(self)
        movie.add_review(self)


    # rating property goes here!
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if (type(rating) == int) and 0 < rating < 6:
            self._rating = rating
        else:
            raise Exception("Ratings must be integers between 1 and 5!")

    # viewer property goes here!

    # movie property goes here!
