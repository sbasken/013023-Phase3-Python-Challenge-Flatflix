#!/usr/bin/env python3
import ipdb
from classes.movie import Movie
from classes.review import Review
from classes.viewer import Viewer


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###

    m1 = Movie("Zoolander")
    m2 = Movie("ABCDE")

    v1 = Viewer("kokotaro")
    v2 = Viewer("sakiboo")

    r1 = Review(v1, m1, 5)
    r2 = Review(v2, m1, 5)
    r2 = Review(v1, m2, 3)
    r2 = Review(v2, m2, 5)









# DO NOT REMOVE THIS
    ipdb.set_trace()
