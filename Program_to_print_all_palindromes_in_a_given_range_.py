n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    temp=i
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
        if i==rev:
            print(i,end=" ")