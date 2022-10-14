def leni(n):
    c = 0
    while n:
        c+=1
        n//=10
    return c

n = int(input())
x = list(map(int,input().split()))
mc = 0
for i in x:
    if leni(i)>mc:
        mc = leni(i)
c=0
for i in x:
    if leni(i)==mc:
        c+=1
print(c)