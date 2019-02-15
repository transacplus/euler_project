"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
from math import sqrt

for b in range(1000):
    for c in range(1000):
        if b < c:
            a = sqrt(c*c-b*b)
            if a < b:
                valeur = a + b + c
                if valeur == 1000:
                    print("%d + %d + %d = 1000" % (1000-b-c, b, c))
                    print("abc = %d" % ((1000-b-c)*b * c))
                    exit
