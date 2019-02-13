"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from math import sqrt


def prime(n):
    """ 
    return true si n est premier 
    """
    if n % 2 == 0:
        return (n == 2)
    # règle dxd < n
    # on peut cesser la recherche d'un diviseur dès que d2 > n.
    #  En effet, si n est composite, c'est-à-dire produit de deux facteurs (différents de 1),
    # le plus petit d'entre eux est inférieur ou égal à la racine carrée de n
    d = int(sqrt(n)+1)
    for i in range(3, d+1, 2):
        if n % i == 0:
            return False

    return True


def pgcd(a, b):
    return a if b == 0 else pgcd(b, a % b)


def decompose(n):
    lstpremier = []
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                if prime(i):
                    lstpremier.append(i)
                    n = n//i
                    if n == 1:
                        break
    return sorted(lstpremier)


dico = {}

for i in range(2, 21):
    dico[i] = decompose(i)
dico_premier = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0}

"""
dico {2: [2], 3: [3], 4: [2, 2], 5: [5], 6: [2, 3], 7: [7], 8: [2, 2, 2],
 9: [3, 3], 10: [2, 5], 11: [11], 12: [2, 2, 3], 13: [13], 14: [2, 7], 
 15: [3, 5], 16: [2, 2, 2, 2], 17: [17], 18: [2, 3, 3], 19: [19], 20: [2, 2, 5]}
"""

for j in dico:
    #print (j)
    # on est dans la decomposition de facteurs premiers
    tmp = {}
    for k in dico[j]:
        tmp[k] = tmp.get(k, 0) + 1

    for premier, nombre in dico_premier.items():
        nbre_puissance = tmp.get(premier, 0)
        if nbre_puissance > nombre:
            dico_premier[premier] = tmp[premier]


x = 1
for premier, nombre in dico_premier.items():
    x *= premier**nombre
print("ppcm de 20 nombres:%d" % x)
print(dico_premier)

# preuve :
l = [x for x in range(2, 21)]
for d in l:
    print("%d / %d = %d " % (x, d, x/d))
