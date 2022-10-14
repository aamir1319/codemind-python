n = int(input())
x = list(map(int,input().split()))

for i in range(n-1):
    if x[i]<x[i+1]:
        print('no')
        break
else:
    print('yes')