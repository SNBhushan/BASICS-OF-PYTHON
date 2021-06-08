usr=int[-9,1,8,2,-7,3,6,-4,5]

print("original list :",usr)

s_d=sorted(usr)
print("the sorted value is :",usr)
if usr < 0:
    print("negative nums:",usr)
else:
    print("the positive nums:",usr)