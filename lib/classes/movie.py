class Movie:
    
    def __init__(self, title):
        self.title = title

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

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
