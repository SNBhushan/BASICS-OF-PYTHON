import re
print("month and day")
s="thse are the dates June 26, August 9, Dec 15"
lstwords=re.finditer(r"([A-Z][a-z]+\s(\d{2})",s)
print(lstwords)


for items in lstwords:
    print("match found at index start{},end {}".format(items.start(),items.end()))
    print("element:",s[items.start():items.end()])
    print("match found {}".format(items.group(0)))

