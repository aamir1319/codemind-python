n = int(input())

nj = 1
for i in range(n-1):
    nj+=2
    
nk=n
nl = n
for i in range(n,0,-1):
    for k in range(n,nk,-1):
        print(k,end=' ')
    nk-=1
    for j in range(nj):
        print(i,end=' ')
    nj-=2
    for l in range(nl+1,n+1):
        print(l,end=' ')
    nl-=1
    print()
    
nj=1
nk=1
nl=2
for i in range(2,n+1):
    # if i!=n:
    for k in range(n,nk,-1):
        print(k,end=' ')
    nk+=1
    for j in range(nj):
        print(i,end=' ')
    nj+=2
    for l in range(nl,n+1):
        print(l,end=' ')
    nl+=1
    print()