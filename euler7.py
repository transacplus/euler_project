"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
"crible Eratosthène"
n = 150000
P = [True] * (n+1)
premier = [2]
for i in range(3, n+1, 2):
    # si le nombre n'est pas rayé il est premier
    if P[i]:
        premier.append(i)
        if len(premier) == 10001:
            print(premier)
            print("The 10 001st prime number is %d" % i)
            break
        # on va rayer ses multiples
        for i in range(2*i, n+1, i):
            P[i] = False
