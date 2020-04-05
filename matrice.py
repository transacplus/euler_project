M=[[0 for j in range(10)] for i in range(3)]
print (M)
M=[[i+j for j in range(10)] for i in range(3)]
print (M)
M=[[1,2,3],
[4,5,6],
[7,8,9]]
#lecture diag
for i in range (3):
        print (M[i][i])
print (M[1][2]) 

