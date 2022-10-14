n,k = map(int,input().split())

x= list(map(int,input().split()))
# print(x,k)
c=0
for i in x:
    if i<0:
        i*=-1
    if k==len(list(str(i))):
        c+=1
print(c)