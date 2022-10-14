def int_len(n):
    c=0
    while n:
        c+=1
        n//=10
    return c
n = int(input())
x = list(map(int,input().split()))
mc = 100
for i in x:
    if int_len(i)<mc:
        mc=int_len(i)
c=0
for i in x:
    if int_len(i)==mc:
        c+=1
print(c)