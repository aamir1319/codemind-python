from itertools import permutations
n,k=map(int,input().split())
x=list(permutations(range(1,n+1)))
for i in x[k-1]:
    print(i,end='')