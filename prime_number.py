def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n//2)+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
if prime(n):
    print("prime")
else:
    print("not a prime")