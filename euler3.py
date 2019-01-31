"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def prime (n):
    """ 
    return true si n est premier 
    """
    if n%2 ==0 :
        return (n==2)
    
    for i in range (3, n, 2):
        if n%i==0:
            return False
        if i*i > n :
            break
    return True


n= 600851475143
lstpremier=[]

while n>1 :
    for i in range (2,n+1):
        if n%i==0  :
            if prime(i) :
                lstpremier.append(i)                
                n=n//i
                if n==1 :
                    break

# le plus grand et le dernier              
print (lstpremier[-1])
m=1
# preuve
for x in lstpremier:
    m=m*x
print (m)
