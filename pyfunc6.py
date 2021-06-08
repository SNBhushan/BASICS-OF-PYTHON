def mysquare(num):
    return num*num

f = lambda num :  num * num
type(f)
print(f)
result=f(5)
print(result)


print((lambda num :  num * num)(10))