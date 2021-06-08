def EmptyListAsParam(mylist=[]):
    if mylist is None:
        mylist=[]
    mylist.append("&")

    return mylist
# always use mylist=none
r1=EmptyListAsParam()
print(r1)
r2=EmptyListAsParam([1,2,3])
print(r2 )