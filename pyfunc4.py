# recursion factorial
def refacto(num):
    if num==0 or num==1:
        return 1
    else:
        return num * refacto(num-1)


n=int(input("enter the value :"))
output=refacto(n)
print(output)