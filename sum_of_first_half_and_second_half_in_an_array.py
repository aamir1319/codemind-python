n = int(input())
x = list(map(int,input().split()))
s,sm = sum(x[:n//2]),sum(x[n//2:])
print(s)
print(sm)