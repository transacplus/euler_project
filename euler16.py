# Euler 16
# 2 ^ 1000
# puis somme des chiffres
# Multiplication 

def n_puissance_p(n,p):
    """ n^p  implémentation de la multiplication avec gestion de la retenue """
    lx=[1]
    lx2=[]
    retenue =0

    for j in range(p):
        for i in lx[::-1] : # parcours inverse de la liste
            t=i*n + retenue
            if t < 10:
                lx2.insert(0,t)
                retenue = 0
            else :
                strvaleur= str(t)
                lx2.insert(0, int(strvaleur[1]))
                retenue = int(strvaleur[0])

        if retenue !=0 :
            lx2.insert(0,retenue)
        retenue = 0
        lx=lx2
        lx2=[]
    return lx

print ((n_puissance_p(2,1000)))  
print (sum(n_puissance_p(2,1000)))       

# implementation triviale avec python ;-) !

y=2**1000
l=[int(i) for i in str(y)]
print (l)
print (sum(l))



    