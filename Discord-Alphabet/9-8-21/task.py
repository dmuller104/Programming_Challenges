# algorithm from: 
# https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0
import numpy as np
def lev_distance(a,b):
    if 0 in [len(a),len(b)]:
        return max([len(a),len(b)])

    paths = np.array([[None]*len(a)]*len(b))
    paths = np.concatenate([[range(1,len(a)+1)],paths])
    paths = np.concatenate([[[i] for i in range(len(b)+1)],paths],1)

    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            paths[i][j] = min([
                paths[i-1][j] + 1,
                paths[i][j-1] + 1,
                paths[i-1][j-1] + (1 if a[j-1] != b[i-1] else 0)
            ])
    return paths[-1][-1]

for a,b in [
    ("kitten", "sitting"),
    ("bounce", "money"),
    ("To be, or not to be, that is the question", "I think, therefore I am"),
    ("Lexyth is bad at math", "Lexyth is cool"), # (:
    ("AlphaBet", "BetAlpha")
]:
    print(lev_distance(a,b),f'"{a}" : "{b}"')

    # paths = np.Array([[i+1] for i in range(len(b))])
    # paths.concatenate
    # return paths