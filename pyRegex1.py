import re
s="welcome     to python  sesti   programming"

print("the value of s:",s)

lst=re.split(r"",s)
print("teh value :",lst)

lst=re.split(r"\s+",s)
print("teh value '\s' :",lst)


lst=re.split(r"(\s+)",s)
print("teh value ('\s+') :",lst)

lst=re.split(r"(s+)",s)
print("teh value ('s+') :",lst)


s="welcome to python programming"
lst=re.split(r"[a-f] [l-n]",s)
print("teh value'555 [a-t] :",lst)

lst=re.split(r"([a-g])",s)
print("teh value '([a-t])' :",lst)

lst=re.split(r"([a-g]|[l-n])",s)
print("teh value '([a-t])' :",lst)

lst=re.split(r"[a-z ]",s)
print("teh value ('s+') :",lst)

