n=int(input())
temp=n
rev=0
while temp:
    rev=rev*10+temp%10
    temp//=10
print(rev)