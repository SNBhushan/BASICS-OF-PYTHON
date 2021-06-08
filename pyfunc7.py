#function as paramter
def mysquare(num):
    return num*num
def mycube(n):
    return n*n*n


def wrapperfun(funasparm,num):
    print("type of fun:",type(funasparm))
    return funasparm(num)


result=wrapperfun(mysquare,(10))
print("result:",result)
list=[mysquare,mycube]
for elments in list:
    print("results:",elments(5))