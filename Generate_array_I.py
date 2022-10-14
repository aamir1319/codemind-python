n = int(input())
x = list(map(int,input().split()))
for i in range(0,n,2):
    for j in range(x[i+1]):
        print(x[i],end=' ')