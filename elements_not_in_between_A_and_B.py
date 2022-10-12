n = input()
x = list(map(int,input().split()))

a,b = map(int,input().split())
t = [i for i in range(a,b+1)]
f=1
for i in x:
    if i not in t:
        f=0
        print(i,end=' ')
if f:
    print(-1)