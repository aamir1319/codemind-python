for o in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    if sorted(x)==x:
        print('0')
    else:
        print(max(x)-min(x))