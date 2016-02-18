HOMEWORK 1

1.
a) f = Θ(g)
b) f = O(g)
c) f = Θ(g)
d) f = Θ(g)
e) f = Θ(g)
f) f = Θ(g)
g) f = Ω(g)
h) f = Ω(g)
i) f = Ω(g)
j) f = Ω(g)
k) f = Ω(g)
l) f = O(g)
m) f = O(g)
n) f = Θ(g)
o) f = Θ(g
p) f = O(g)
q) f = Θ(g)

2.
Since 31 is prime, 5^(31 – 1) ≅ 1 mod (31) and 6^(31 – 1) ≅ 1 mod(31). 
Therefore, 5^30,000 ≅ 1 mod(31) since 30,000 is a multiple of 30. 
6^123,456 = 6^123,450 * 6^6. 
6^123,450 ≅ 1 mod(31) since 123,450 is a multiple of 30.
Similarly, 6^6 ≅ 1 mod(31).
Therefore it follows that 6^123,450 * 6^6 ≅ 1 mod(31).
Thus, 6^123,450 – 5^30,000 ≅ (1-1)mod(31) so it must be a multiple of 31.

3.
Proof:
Let some positive integer n have x digits in binary. Then 2^x is greater than n because we need the smallest power of two that is larger than n. We also know that n > 2^(x-1) except when n is a power of two. Thus n >= 2^(x-1). Therefore, x > log2(n) >= x -1. Finally, this proves that x <= log2(n) + 1. We need log2(n) + 1 digits to represent any given n in binary.

4.
a) To put k grains on the chessboard according to this pattern, it will take 2^(k-1) seconds. Thus for 64 grains, it will take 2^63 seconds. 2^63 seconds equals 9,223,372,036,854,775,808 seconds.
 
b) This is equal to the summation sum_(k=0)^63(2 k+1) = 4096 seconds.

5.
See homework 1 folder

6.
See homework 1 folder

7.
If memoization is not used we will have to recursively call the function 335,919 times to find the answer because each time we call nCr we must call it two more times. With memoization it will only take 199 function calls.

8.
See homework 1 folder
