import re

samplestring=''' 
Rohit made 126 runs , Virat made 136 runs and 
Dhawan made 46 runs and we won the match'''

lstwods=re.findall(r"\d{2,3}",samplestring)
list1=re.findall(r"[A-Z][a-z]+",samplestring)
print(lstwods)
print(list1)


result={}
for items in range(len(lstwods)):
    result[lstwods[items]]=list1[items]

print(result)

result={lstwods[items]:list1[items] for items in range(len(lstwods))}
print(result)

result=zip(lstwods,list1)
print(result) 
