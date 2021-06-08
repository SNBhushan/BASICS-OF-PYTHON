def multipleunpacking(*args):
    print("Type:",type(args))
    print(args)

a=[1,5,6]
multipleunpacking(a)

b=(5,8,9)
multipleunpacking(b)

c={3,7,6}
multipleunpacking(c)

r=range(100,105)
multipleunpacking(*r)

print(*range(1,6),sep="\n")
