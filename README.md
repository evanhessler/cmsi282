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



HOMEWORK 2

3.
THE PROGRESS OF OUR ARMS, UPON WHICH ALL ELSE CHIEFLY DEPENDS, IS AS WELL KNOWN TO THE PUBLIC AS TO MYSELF, AND IT IS, I TRUST, REASONABLY SATISFACTORY AND ENCOURAGING TO ALL. WITH HIGH HOPE FOR THE FUTURE, NO PREDICTION IN REGARD TO IT IS VENTURED.

(-Abraham Lincoln)

4.
COMPUTER SCIENCE IS NO MORE ABOUT COMPUTERS THAN ASTRONOMY IS ABOUT TELESCOPESS

5.
N = p*q = 1911330379750465988511865475607817924950038631764482538080744390093883432017

X = (p-1)(q-1) = 1911330379750465988511865475607817924846043384185557740590270903584228162660

Some E relatively prime to X = 7

D = invmod(E, X) = 1911330379750465988511865475607817924846043384185557740590270903584228162660

Public key = (N, E) = (1911330379750465988511865475607817924950038631764482538080744390093883432017, 5)

Private key = (N, D) = (1911330379750465988511865475607817924950038631764482538080744390093883432017, 1911330379750465988511865475607817924846043384185557740590270903584228162660)

6.
If we factor N = 729880581317 we get N = pq = 822893 * 886969. 
Then (p-1)(q-1) = 729878871456.
Since e = 5, D = invMod(5, 729878871456) = 583903097165.
Thus her private key is (N, D) = (729880581317, 583903097165)

7.
a) 
Digital signatures allow the receiver of a message to determine whether or not the message came from the expected sender; otherwise, the receiver will know if the message has been altered by someone else.

b) ?
c) 
Let p = 97, q = 61, and e = 17. 
Then N = pq = 5,917. 
(p-1)(q-1) = 5,760. 
D = invMod(e, (p-1)(q-1)) = invMod(17, 5760). 17(2,033) = 1mod(5760). Therefore D = 2,033.
Let ‘E’ = m1 = 4, ‘V’ = m2 = 20, ‘A’ = m3 = 0, and ‘N’ = 13.
Then m1^D mod(N) = 4^2,033 mod(5,917) = 2662.
m1^De mod(N) = 4 and m1 mod(N) = 4. Thus m1^De mod(N) = m1 mod(N)

d)
Since N = 391, N can be factored into 23 and 17. 
Therefore (p-1)(q-1) = (22)(16) = 352.
Since e = 17, D = invMod(17, 352) = 145.
Then Alice should raise her message to the exponent DE = (145*17) = 2,465.

8.
a) 
If Alice sends some message M to Bob, Eve can have Bob sign it. This gives Eve M^De mod (N) which gives her M.

b)
?

9.
The program takes 2T(n/2) + Θ(1) amount of work because we have 2 n/2 function calls for each function call and a constant amount of work each time. Thus it is a Θ(n) time algorithm.
