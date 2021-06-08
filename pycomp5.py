
websites=["amazon","flipkart","patym"]
extensions=("org","in","com")

result1=["www."+web+"."+ext for web in websites for ext in extensions]
print(result1 )
for web in websites:
    for ext in extensions:
        print("www." + web + "."+ext)





