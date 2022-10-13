n = int(input())
c=0
x = list(map(int,input().split()))
temp = []
for i in x:
    if i not in temp and i%2==0:
        c+=1
        temp.append(i)
print(c)