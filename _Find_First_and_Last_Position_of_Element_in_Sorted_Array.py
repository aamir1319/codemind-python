n = int(input())
x = list(map(int,input().split()))
tar = int(input())
if tar not in x:
    print(-1,-1)
else:
    print(x.index(tar),n-x[::-1].index(tar)-1)