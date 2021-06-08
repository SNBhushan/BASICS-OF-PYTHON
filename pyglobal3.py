runsscored=1
def localfunction():
    runsscored=2
    print("the value of runsscored in localfunction:",runsscored)

def globalfunction():
    global runsscored
    runsscored=3
    print("the value of runsscored in globalfunction:",runsscored)

print("the value run scored in main:",runsscored)
localfunction()
print("after calling local function,the value of main is :",runsscored)
globalfunction()
print("after calling global function,the value of main is :",runsscored)