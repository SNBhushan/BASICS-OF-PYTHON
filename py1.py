#fibonacci series
#lookup={}
a,b=0,1
for item in range(41):
    print(a,end = " ")
    a,b=b,a+b



def fibo(n):
    if n == 0 or n  == 1:
        return n
    if n not in lookup:
        lookup[n] = fibo(n-1) + fibo(n-2)
    return lookup[n]

num=int(input("enter any number"))
for item in range(num):
    print(fibo(item),end=" ")