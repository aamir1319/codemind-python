n = int(input())
x = list(map(int,input().split()))

s = 0
for i in x:
    temp = i 
    while temp:
        s+=temp%10
        temp//=10

print(s)