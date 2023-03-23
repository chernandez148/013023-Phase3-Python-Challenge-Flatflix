from .review import Review

class Viewer:
    
    def __init__(self, username):
        self.username = username

    # username property goes here!

    def reviewed_movie(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass

viewer1 = Viewer("Chris")
print(viewer1.username)