from functools import reduce
nums=list(range(1,10 ))
print("numbders:",nums)
addons=lambda x,y:x+y
print(addons(100,200))

result=reduce(addons,nums)
print(result)


mul=lambda x,y:x*y
print(mul(100,200))
result=reduce(mul,nums)
print(result)