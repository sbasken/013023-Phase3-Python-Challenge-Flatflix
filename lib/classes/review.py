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
            raise Exception("Rating must be an integer between 1 and 5!")

    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        from .viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewer must be a Viewer instance!")
    

    # movie property goes here!
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        from .movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("Movie must be a Movie instance!")
