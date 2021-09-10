Here is an intermediate task

Levenshtein distance (or edit distance) is one of many measures for finding how "far apart" two strings are, in some sense. There are three operations we can perform on a string:

We can insert a letter at any position,
We can remove a letter at any position,
We can change any one letter.

The Levenshtein distance is how many of these operations it takes to convert one string to another.

Write a function that computes the levenshtein distance of two strings.

Examples
To transform kitten into sitting:
- Change the k to s (sitten)
- Change the e to i (sittin)
- Add a g (sitting)
This comes out to a total distance of 3. Note that the distance is symmetric, changing sitting to kitten also takes 3 steps.

To tranform bounce into money:
- Change the b to m (mounce)
- Remove the u (monce)
- Remove the c (mone)
- Add a y (money)
This makes a Levenshtein distance of 4.

Test cases
```
"kitten", "sitting" -> 3
"bounce", "money" -> 4
"To be, or not to be, that is the question", "I think, therefore I am" -> 33
"Lexyth is bad at math", "Lexyth is cool" -> 11
"AlphaBet", "BetAlpha" -> 6
```

Bonus
- Write an algorithm that is no worse than O(nm), with m and n the lengths of the strings.