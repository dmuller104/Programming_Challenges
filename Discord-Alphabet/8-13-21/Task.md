Here Is Today's Task For Intermediates:
Given N representing the number of pairs of shoes we have and than 2*N numbers, the i-th number representing the colour of the i-th shoe, every shoe can have a colour greater than 0 and smaller than N+1, there are exacly 2 shoes of each colour. We can choose 2 shoes and swap them, the goal is to rearrange the shoes in minimun number of swaps such that every shoe is next to its pair ( the other shoe of the same colour).
Sample Output :-
```
3
1 2 3 1 3 2
➞ 2

Considering the shoes are indexed by 1, we can swap shoe 3 with shoe 4 the arrangement will than be 1 2 3 1 2, swap than the first shoe with the last one, we obtain 2 2 3 3 1 1, this is a valid arrangement, the minimum number of swaps was 2. (there is also no better solution).
```
Notes:-
  - N <= 1.000.000.
Observation:
  - Design an  O(n) algorithm in order to score points.