n=int(input("enter the number"))
rev=0
while(n>0):
    jk=n%10
    rev=rev*10+jk
    n=n//10
print("reverse:",rev)
