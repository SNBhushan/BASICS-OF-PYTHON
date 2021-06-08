#credit card details
import  re
empde=" hi i have a credit card with number 3775 123456 78910"\
      " other card is "\
      " 3545 456789 12345 "


lstwords=re.findall(r"3[4|7]\d{2}\s\d{6}\s\d{5}",empde)
print(lstwords)