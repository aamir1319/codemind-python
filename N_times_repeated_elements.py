n = int(input())
x = list(map(int,input().split()))
k = int(input())
temp = []
for i in x:
    if x.count(i)==k and i not in temp:
        temp.append(i)
        print(i,end=' ')

if len(temp)==0:
    print(-1)