n = int(input())
x = list(map(int,input().split()))
s=c=0
temp = []
for i in x:
    if i not in temp and i==x.count(i):
        temp.append(i)
        s+=i
        c+=1
if c==0:
    print(-1)
else:
    print('{:.2f}'.format(s/c))