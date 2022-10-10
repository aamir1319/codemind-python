def fact(n):
    c =1
    for i in range(2,n+1):
        c*=i
    return c
t = int(input())

for i in range(t):
    print(fact(int(input())))