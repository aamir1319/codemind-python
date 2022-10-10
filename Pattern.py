n = int(input())

nj = n

nk = 1

nl = nk
for i in range(n):
    for j in range(nj-1):
        print(end=' ')
    nj-=1
    for k in range(1,nk+1):
        print(k,end='')
    nk+=1
    for l in range(nl-1,0,-1):
        print(l,end='')
    nl+=1
    print()