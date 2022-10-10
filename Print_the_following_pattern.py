n = int(input())

nj = n

nk = 1

nl = nk

for i in range(n):
    for j in range(nj-1):
        print(end=' ')
    nj-=1
    for k in range(65,65+nk):
        print(chr(k),end='')
    nk+=1
    for l in range(64+nl-1,64,-1):
        print(chr(l),end='')
    nl+=1
    print()
    