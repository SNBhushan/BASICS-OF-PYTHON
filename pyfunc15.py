#new rule has been included in python3.8:positionalkeyword argument

def positionalargument(a,b,/,c,d,*,e,f):
    print("a:{},b:{},c:{},d:{},e:{},f:{}".format(a,b,c,d,e,f))

#positionalargument(1,2,3,4,5,6)
#positionalargument(1,2,c=3,d=5,e=9,f=40)
#positionalargument(a=3,4,3)