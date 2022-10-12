n = int(input())
x = list(map(int,input().split()))

s = 0
p = n-1
for i in range(n):
    s = s + x[i]*(2**p)
    p-=1
print(s)