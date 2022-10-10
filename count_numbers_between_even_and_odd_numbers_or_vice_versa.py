n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if (x[i-1]%2!=0 and x[i+1]%2==0) or  (x[i-1]%2==0 and x[i+1]%2!=0):
        c+=1
print(c)