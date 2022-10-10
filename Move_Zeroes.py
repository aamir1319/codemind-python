n = int(input())

x = list(map(int,input().split()))

for i in range(n):
    for j in range(n-1):
        if x[j]==0:
            x[j],x[j+1] = x[j+1],x[j]
for i in x:
    print(i,end=' ')