user=input("")
print(user)

lts=list(map(int,user.split()))
print(lts)


avg=sum(lts[1:])/lts[0]
print(avg)
