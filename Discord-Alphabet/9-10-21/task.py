# Answer

import numpy as np
from math import gcd

def get_vector(point1,point2):
    vect = np.subtract(point1,point2)
    scalar = gcd(*vect)
    d_vect = vect//scalar
    c = point1 - d_vect * point1[0]
    return (tuple(c),tuple(d_vect))

def any_three_toilet(points):
    vectors = set()
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            slopevector_const = get_vector(points[i],points[j])
            if slopevector_const in vectors:
                return True
            else:
                vectors.add(slopevector_const)
    return False

for l in [
    [(1, 1), (2, 3), (3, 5)],
    [(1, 1), (2, 3), (3,4)],
    [(1,10), (8,-9), (-2,0), (-5,6), (-8,-6)],
    [(-9,7), (2,2), (9,-5), (-3,7), (-8,-10)],
    [(-1, 0), (0, 3), (9, 0), (6, -1), (-2, -1), (-9, -7), (-6, -9), (5, -4), (9, 2), (7, -5)],
    [(-2, 9), (1, -3), (7, -5), (-10, 7), (8, 7), (-1, 0), (2, -6), (-7, -9), (5, -1), (3, -1)],
    [(7, -9), (7, 4), (-9, -6), (7, -8)],
    [(-2, 9, 4), (1, -3, 1), (7, -27, -4)],
    [(1, 1, 1, 1, 1), (2, 0, 1, 3, -1), (3, -1, 1, 5, -3)]
]:
    print(f"{l} {'True' if not any_three_toilet(l) else 'False'}")
