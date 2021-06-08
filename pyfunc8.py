def sumofnum(a,b,c):
    print("result:",a+b+c)
sumofnum(1,5,6)


def sumofnum(*args):
    print("Args:",args)
    print("Type(Args):",args)
    result=0
    for items in args:
        result=result+items
        print("RESULT:",result)
sumofnum(1,5,5)

