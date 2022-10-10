def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True

def reverse(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    return rev


p=int(input())
if prime(p) and prime(reverse(p)):
        print("circular prime")
elif prime(p):
    print("prime but not a circular prime")
else:
    print("not prime")
        