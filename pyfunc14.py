#new rule has been included in python3.8

def positionalargument(a,b,/,c):
    print("a:{},b:{},c:{}".format(a,b,c))

positionalargument(1,2,3)
positionalargument(1,2,c=3)
positionalargument(a=3,4,3)