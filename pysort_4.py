# sorting based on key params
usr=[5,6,-8,9,-3,-1,4,7]
print("original list:",usr)

s_lt=sorted(usr,key=abs)  # Non inplace sorting

print("sorted list :",s_lt)
print("original list:",usr)

#print("the sorted value")
#usr.sort() #inplace sorting
#print("original list:",usr)