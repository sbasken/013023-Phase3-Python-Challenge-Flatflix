class Review:
    
    def __init__(self, viewer, movie, rating):
        if not 1 <= rating <= 5:
            raise Exception("rating must be between 1 and 5")
        
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        viewer.add_review(self)
        movie.add_review(self)

    # rating property goes here!

    # viewer property goes here!

    # movie property goes here!
