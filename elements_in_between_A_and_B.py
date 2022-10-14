n = int(input())
x = list(map(int,input().split()))
a,b = map(int,input().split())
s = 0
e = 0
f=0
for i in x:
    if i>=a and i<=b:
        # print(i>=a,i,a,b,i<=b)
        print(i,end=' ')
        f=1
if not bool(f):
    print(-1)