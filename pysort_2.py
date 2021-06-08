usr=[5,6,8,9,3,1,4,7]
print("original list:",usr)

s_lt=sorted(usr,reverse=True)  # Non inplace sorting

print("sorted list :",s_lt)
print("original list:",usr)

print("the sorted value")
usr.sort(reverse=True)  #inplace sorting
print("original list:",usr)