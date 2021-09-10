Let's try some simple computational geometry.

You will be given a set of points. You may assume all points are distinct and have integer components. Your task is to determine whether any triplet of points in the set are collinear -- that is, whether any 3 of them lie on the same line. For example, the trio of points [(1, 1), (2, 3), (3, 5)] is collinear, but the trio [(1, 1), (2, 3), (3,4)] is not.

```
Test cases
[(1, 1), (2, 3), (3, 5)] -> True
[(1, 1), (2, 3), (3,4)] -> False
[(1,10), (8,-9), (-2,0), (-5,6), (-8,-6)] -> False
[(-9,7), (2,2), (9,-5), (-3,7), (-8,-10)] -> True
[(-1, 0), (0, 3), (9, 0), (6, -1), (-2, -1), (-9, -7), (-6, -9), (5, -4), (9, 2), (7, -5)] -> True
[(-2, 9), (1, -3), (7, -5), (-10, 7), (8, 7), (-1, 0), (2, -6), (-7, -9), (5, -1), (3, -1)] -> False
[(7, -9), (7, 4), (-9, -6), (7, -8)] -> True
```

Bonus
- Write an algorithm that is no worse than O(n^2), with n the number of points.

Note
Be especially careful about how you handle vertical lines. They may be tricky depending on your implementation.
