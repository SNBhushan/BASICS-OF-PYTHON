try:

    user=input("enter any numbser:")
    result=100/int(user)
    print(result)

except ValueError:
    print("please enter only numbers")

except ZeroDivisionError:
    print("plaese enter number greater tahn zero")