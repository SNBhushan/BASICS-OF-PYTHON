import re
s="Abc welcome 2Check paT3en ano3ter check3alTd 22Checj B5 8C"

lst=s.split()
print(lst)

for items in lst:
    patmatched = re.search(r"(.*[A-Z].*\d.*)|(\d{2}[A-Z].*)|(.*\d{1}.*[A-Z].*)|([A-Z][a-z].*)",items)
    if patmatched:
        print(patmatched.group(0))