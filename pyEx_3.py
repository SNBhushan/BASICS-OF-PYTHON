try:
    result=(item*item for item in range(10000000 ))
    print(result)
    for item in result:
        print(item)
except MemoryError:
    print("value exceeded")
