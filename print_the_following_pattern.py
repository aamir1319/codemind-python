n=int(input())
for i in range(n,0,-1):
    for _ in range(i,1,-1):
        print(end=' ')
    for j in range(n):
        if i==1 or i==n or j==0 or j==n-1:
            print('*',end='')

        else:
            print(end=' ')
    print()        