for o in range(int(input())):
    n,m=map(int,input().split())
    for i in range(0,max(n,m)):
        if (i*i)%m==n:
            print(i)
            break
    else:
        print(-1)
        