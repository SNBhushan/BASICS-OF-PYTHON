import re
s=" computer1: 10.67.89.101, 11.67.98.102,12.68.98.102  "
lst=re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.)",s)
print("teh value is:",lst)

lst=re.findall(r"10\.\d{1,3}\.\d{1,3}\.)",s)
print("teh value is:",lst)

