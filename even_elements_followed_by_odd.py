n  = int(input())
x = list(map(int,input().split()))

for i in range(n):
    if x[i]%2==0:
        print(x[i],end=' ')
for i in range(n):
    if x[i]%2==1:
        print(x[i],end=' ')