"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
O(n2)
"""
palindrome=0
t=()
for i in range(100,1000):
    for j in range (100,1000):
        val = i*j
        # mise en tableau pour comparaison 
        liste_strval= list(str(val))
        reverse_strval= liste_strval[::-1]
        if liste_strval ==  reverse_strval :
            #print (str((i,j,val)))
            if val > palindrome :
                palindrome=val
                t=(i,j,val)

print ("Le palindrome le plus grand : %d x %d = %d"   % t )
