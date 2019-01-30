list=[]
for i in range(1000):
    if i%3 == 0 :
        list.append(i)
    if i%5 == 0 :
        list.append(i)
print(list)
print (" Somme des éléments %s " % sum(list) )
