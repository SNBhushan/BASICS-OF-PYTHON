# factorial of a number
def factorial(num):
    result = 1
    for item in range (1,num+1):
        result=result*item


    return result

num =int(input("enter the value:"))
out=(factorial(num))
#print(out)
print("factorial of {} is {}".format(num,out))