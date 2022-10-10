def selfdiv(n):
    temp=n
    while temp:
        a=temp%10
        if a==0:
            return False
        elif n%a!=0:
            return False
        temp//=10
    return True
n1=int(input())
n2=(int(input()))
for i in range(n1,n2+1):
    if selfdiv(i):
        print(i,end=" ")