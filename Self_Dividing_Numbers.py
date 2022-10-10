def sdn(n):
    temp =n
    while temp:
        z = temp%10
        if z==0:
            return False
        elif n%(z)!=0:
            return False
        temp//=10
    return True

a = int(input())
b = int(input())

for i in range(a,b+1):
    if sdn(i):
        print(i,end=' ')