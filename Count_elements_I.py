n,m = map(int,input().split())

x = list(map(int,input().split()))
l = list(map(int,input().split()))

c=0
temp = []
for i in x:
    if i in l and i not in temp:
        temp.append(i)
        c+=1
print(c)