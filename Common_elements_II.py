n,m = map(int,input().split())

x = list(map(int,input().split()))
y = list(map(int,input().split()))
temp = []
for i in x:
    if i not in y and i not in temp:
        temp.append(i)
for i in y:
    if i not in  x and i not in temp:
        temp.append(i)
        
for i in temp:
    print(i,end=' ')