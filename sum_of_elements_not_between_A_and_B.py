n = input()
x = list(map(int,input().split()))

a,b = map(int,input().split())
s=0
z = sum(x)
for i in range(a,b+1):
    if i in x:
        s+=i
print(abs(s-z))