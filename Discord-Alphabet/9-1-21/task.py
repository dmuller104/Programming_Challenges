from math import comb
def safeknight(n:int)->int:
    return comb(n**2,2) - (0 if n<=2 else (n-2)**2*8)

for i in range(11):
    print(i,safeknight(i))