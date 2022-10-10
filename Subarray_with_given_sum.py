for i in range(int(input())):
    n,s= map(int,input().split())
    x = list(map(int,input().split()))
    for i in range(n):
        sm = 0
        f=0
        for j in range(i,n):
            sm+=x[j]
            if sm==s:
                print(i+1,j+1)
                f=1
                break
        if f==1:
            break
    else:
        print(-1)