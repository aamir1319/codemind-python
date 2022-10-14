n,m = map(int,input().split())

x = list(map(int,input().split()))
y = list(map(int,input().split()))
temp = []
for i in x:
    if i in y and i not in temp:
        temp.append(i)
for i in temp:
    print(i,end=' ')