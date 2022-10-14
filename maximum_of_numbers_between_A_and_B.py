n = int(input())
x = list(map(int,input().split()))
a,b = map(int,input().split())
m = a
for i in x:
    if i>=a and i<=b and m<i:
        m=i
if m==a:
    print(-1)
else:
    print(m)