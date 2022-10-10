def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

n = int(input())
temp = n
s = 0
while temp:
    s+=fact(temp%10)
    temp//=10

if s==n:
    print('The number',n,'is a strong number')
else:
    print('The number',n,'is not a strong number')