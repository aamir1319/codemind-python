def prime(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n):
    while(n!=0):
        rem=n%10
        n//=10
        if not prime(rem):
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")