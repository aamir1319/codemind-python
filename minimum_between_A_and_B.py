n = int(input())
x = list(map(int,input().split()))
a,b = map(int,input().split())

m = b

for i in x:
    if i>=a and i<=b and i<m:
        m=i
if m==b:
    print(-1)
else:
    print(m)