n = int(input())

x = list(map(int,input().split()))
nw = []
for i in range(n):
    s=1
    for j in range(n):
        if i!=j:
            s*=x[j]
    nw.insert(i,s)
for i in nw:
    print(i,end=' ')