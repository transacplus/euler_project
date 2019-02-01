"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
from math import sqrt
def prime (n):
    """ 
    return true si n est premier 
    """
    if n%2 == 0 : return (n==2)
    # règle dxd < n
    # on peut cesser la recherche d'un diviseur dès que d2 > n.
    #  En effet, si n est composite, c'est-à-dire produit de deux facteurs (différents de 1), 
    # le plus petit d'entre eux est inférieur ou égal à la racine carrée de n
    d=int(sqrt(n)+1)
    for i in range (3, d+1, 2):
        if n%i==0:
            return False
       
    return True

def pgcd (a,b) :
    return a if b == 0 else pgcd(b, a%b)

def decompose (n):
    lstpremier=[]
    while n>1 :
        for i in range (2,n+1):
            if n%i==0  :
                if prime(i) :
                    lstpremier.append(i)                
                    n=n//i
                    if n==1 :
                        break
    return sorted(lstpremier)


n= 600851475143

# le plus grand et le dernier              
result =decompose(n)
print (result)

