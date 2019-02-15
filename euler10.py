"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
"crible Eratosthène"
n = 2000000
P = [True] * (n+1)
premier = 2
for i in range(3, n+1, 2):
    # si le nombre n'est pas rayé il est premier
    if P[i]:
        premier += i
        # on va rayer ses multiples
        for i in range(2*i, n+1, i):
            P[i] = False
print("Somme des nombres premiers inférieurs à 2 000 000 : %d" % premier)
