result=[]
for items in range (1,11):
    result.append(items*items)
print(result)

result=[items*items for items in range(1,11)]
print(result)

print(items*items for items in range (1,11))
