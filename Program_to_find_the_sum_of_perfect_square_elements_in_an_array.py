n = int(input())
x = list(map(int,input().split()))

m = max(x)
s = 0
for i in range(1,m//2):
    if i*i in x:
        s+=i*i
print(s)