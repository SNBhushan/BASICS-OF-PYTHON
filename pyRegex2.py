import re
address="72, btm layout 1st stage 2nd cross oppsite to 10 main 560068  "

lst=re.findall(r"\d",address)
print(" teh value of '\d':",lst)


lst=re.findall(r"\d+",address)
print(" teh value of '\d+':",lst)


lst=re.findall(r"\d{6}",address)
print(" teh value of '\d{}':",lst)


lst=re.findall(r"\d{2}",address)
print(" teh value of '\d{}':",lst)

lst=re.findall(r"\s(\d{2})\s",address)
print(" teh value of '\d{}':",lst)

lst=re.findall(r"\s\d{2}\s",address)
print(" teh value of '\d{}':",lst)