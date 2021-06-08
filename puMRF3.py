nums=list(range(1,11))
print("numbers:",nums)
even=lambda num:num %2==0
print(even(5))
print(even(10))
result=map(even,nums)
print("using map:",result)
print(type(result))
print(list(result))