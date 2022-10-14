def leng(n):
    if n==0:
        return 1
    if n<0:
        n*=-1
    c=0
    while n:
        c+=1
        n//=10
    return c

n = int(input())
x = list(map(int,input().split()))

for i in x:
    print(leng(i),end=' ')