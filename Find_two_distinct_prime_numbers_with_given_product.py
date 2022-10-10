def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
flag=0
for i in range(1,n):
    for j in range(1,n):
        if i*j==n :
            if prime(i) and prime(j):
                print(i,j)
                flag=1
                break
    if flag==1:
        break
else:
    print(-1)