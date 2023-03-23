class Review:
    
    def __init__(self, viewer_instance, movie_instance, rating):
        self.viewer = viewer_instance
        self.movie = movie_instance
        self._rating = rating

    @property 
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if 1 < rating < 6:
            self._rating = rating
        else:
            raise Exception("requires ratings to be between 1 and 5, inclusive.")

    # viewer property goes here!

    # movie property goes here!

ri = Review(chris, v for vendetta, 4)
print(r1.viewer)
