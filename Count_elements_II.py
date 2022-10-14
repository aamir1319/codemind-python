n = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
temp = []
for i in x:
    if i not in temp and i not in y:
        temp.append(i)
for i in y:
    if i not in temp and i not in x:
        temp.append(i)
print(len(temp))