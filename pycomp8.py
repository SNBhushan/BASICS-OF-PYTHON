s=" i want a data analyst job"
result={item:s.count(item) for item in s}
print(result)
result={}
for item in s:
    result[item]=item.count(s)

print(result)