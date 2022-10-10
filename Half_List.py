n = int(input())
a = n//2
x = list(map(int,input().split()))

for i in range(n-1,a-1,-1):
    print(x[i],end=' ')
for i in range(a):
    print(x[i],end = ' ')