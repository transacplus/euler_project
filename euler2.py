
"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding
the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.
"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


list =[1,2]
i=2
term = 0
while True :
    term= list[i-1] + list[i-2]
    if term < 4000000 :
        list.append(term)
        i+=1
    else:
        break
 
print (list)
print (" Somme des éléments des termes n exedant pas 4 000 000 : %s " % sum(list) )
print (fibo(100))
