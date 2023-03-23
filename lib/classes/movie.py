from .review import Review

class Movie:
    
    def __init__(self, title):
        if isinstance(title, str) and 0 < len(title):
            self.title = title
        else: 
            raise Exception("requires titles to be strings of >0 characters.")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass

movie1 = Movie("v for vendetta")
print(movie1.title)