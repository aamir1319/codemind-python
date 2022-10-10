n=int(input())
x=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if x[i]%2==1:
        print(i)
        break