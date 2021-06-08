import re
s="purple alice@googlr.com  abcdce helloab@abc.com gdhjs "
lsr=re.findall(r"[a-z]+@[a-z]\.[a-z]+",s)
print(lsr)