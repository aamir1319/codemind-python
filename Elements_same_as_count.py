n = int(input())
x = list(map(int,input().split()))
temp = []
for i in x:
    if i not in temp and i==x.count(i):
        temp.append(i)
        print(i,end=' ')
if len(temp)==0:
    print(-1)