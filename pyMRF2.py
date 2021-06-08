nums=list(range(1,11))
print("numbesr:",nums)

sq=lambda num:num*num
mobject=map(sq,nums)
print(mobject)
print(type(mobject))
print(list(mobject))