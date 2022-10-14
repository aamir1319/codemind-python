def rev(n):
    reve = 0
    while n:
        reve=reve*10 + n%10
        n//=10
    return reve

n = int(input())
x = list(map(int,input().split()))

for i in x:
    print(rev(i),end=' ')