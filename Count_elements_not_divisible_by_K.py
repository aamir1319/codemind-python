n,k = map(int,input().split())
x = list(map(int,input().split()))
c=0
for i in x:
    if i%k!=0:
        c+=1
print(c)