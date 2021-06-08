#prime numbers
# for item in range(100,200)
# check whetre it is divsible by 2 to 99
 
for items in range(100,200):
    isprime =True
    for idiv in range(2,items):
        if items % idiv == 0:
            isprime= False
            break
    if isprime:
        print(items,end=" ,")
