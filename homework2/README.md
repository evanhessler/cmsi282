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
