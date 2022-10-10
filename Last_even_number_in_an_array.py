n=int(input())
x=list(map(int,input().split()))
a=x[::-1]
for i in a:
    if i%2==0:
        print(i)
        break