n = int(input())
x = list(map(int,input().split()))
c =0
temp = []
for i in x:
    if i == x.count(i) and i not in temp:
        c+=1
        temp.append(i)
print(c)