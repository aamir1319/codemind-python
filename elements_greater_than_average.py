n = int(input())
x = list(map(int,input().split()))

avg = sum(x)//n
c=0
for i in x:
    if i>=avg:
        c+=1
print(c)