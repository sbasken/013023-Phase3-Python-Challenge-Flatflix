class Viewer:

    usernames = []
    
    def __init__(self, username):
        self.username = username

        Viewer.usernames.append(self.username)

    # username property goes here!
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if (not username in Viewer.usernames) and (6 <= len(uv1sername) <= 16):
            self._username = username
        else:
            raise Exception("Usernames must be unique strings between 6 and 16 characters!")


    def reviewed_movie(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass