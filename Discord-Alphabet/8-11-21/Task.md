Here's a Task for Intermediate

One operation that is particularly common in calculus is to differentiate polynomials. I'll leave off why this particular operation is so common (research Taylor Series if you're interested), and jump straight into how to actually do it.

In calculus, to differentiate a polynomial, you need two rules:
1. The derivative of a sum is the sum of the derivatives: that is, (f + g)' = f' + g', where ' means derivative.
2. The derivative of a monomial: a * x^b = a * b * x^(b-1).

Note: There are special cases for x^1 (which is just x), and x^0 (which is just 1). Another special case is that the derivative of a constant is 0.

Your goal is to write a function that takes the derivative of a provided polynomial. The polynomial will have one variable (which is some lowercase letter), and its coefficients and exponents will always be constants.

Test Cases
```
derivative("2x^2 + 3x + 2") == "4x + 3"
derivative("4y^3 + 2y^2 + 4") == "12y^2 + 4y"
derivative("20x^20 + 19x^15") == "400x^19 + 285x^14"
derivative("z^3 + z^2 + z + 1") == "3z^2 + 2z + 1"
derivative("1 + 14x + 2x^3") == "6x^2 + 14"
derivative("1") == "0"
```

Bonus
Handle arbitrary whitespace around the expressions (with the exception of the numbers never being broken up). So the derivative of 2x^3+3x+1 is the same as the derivative of 2 x ^ 3 + 3 x + 1. If not going for this bonus, whitespace rules are up to your preference.

Notes
As usual, I'll do code review of solutions on request. Meme submissions don't count.