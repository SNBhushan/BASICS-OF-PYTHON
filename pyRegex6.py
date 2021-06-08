import re
print("month and day")

lstwords=re.findall(r"[A-Z][a-z]+\s(\d{2})","thse are the dates June 26, August 9, Dec 15")
print(lstwords)

lstwords=re.findall(r"([A-Z][a-z])+\s(\d{2})","thse are the dates June 26, August 9, Dec 15")
print(lstwords)