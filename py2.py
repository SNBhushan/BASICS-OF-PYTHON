#palimdrome

# def ispalindrome(s):
#     s=s.lower()
#     for item in range(len(s)//2):
#         if s[item]!=s[len(s)-item-1]:
#             return False
#     return True
def ispalindrome(s):
    s=s.lower()
    return s==s[::-1]
s="madam"
print(ispalindrome(s))

