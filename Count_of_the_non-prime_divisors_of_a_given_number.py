def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True 
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if not prime(i):
            c+=1
print(c)