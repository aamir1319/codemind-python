n = int(input())
x = list(map(int,input().split()))

for i in x:
        print(i,end=' ')

if n%2==1:
    print(0)