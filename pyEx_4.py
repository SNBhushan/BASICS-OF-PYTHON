try:
    fh=open("exceptinalhanding.txt","w")
    fh.write("opening the new file.\n")
    fh.write("enter the number\n")
    user=input("enter any numbser:")
    fh.write("the entered number is:"+user+"\n")

    result=100/int(user)
    fh.write("the result is :"+str(result)+"\n")
    print(result)
    fh.write("closing the file.")
    fh.close()

except ValueError:
    print("please enter only numbers")

except ZeroDivisionError:
    print("plaese enter number greater tahn zero")

finally:
    fh.write("close the file\n")
    fh.close()