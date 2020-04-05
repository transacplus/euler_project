"crible Eratosthène"
n=100000
P=[True] * (n+1)
premier=[2]
for i in range (3,n+1,2):
 #si le nombre n'est pas rayé il est premier
 if P[i] :
    premier.append(i)
    #on va rayer ses multiples
    for i in range(2*i,n+1,i):
        P[i]=False
print (premier)
        
 