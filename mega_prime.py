def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n):
    while(n!=0):
        res=n%10
        n//=10
    if(prime(res)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")