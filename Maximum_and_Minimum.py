n = int(input())
x = list(map(int,input().split()))
temp = []
for i in x:
    if i not in temp and i==x.count(i):
        temp.append(i)
if len(temp)==0:
    print(-1)
else:
    print(min(temp),max(temp))