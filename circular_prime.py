def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def REV(n):
    temp = n
    rev = 0
    while temp:
        rev = rev*10 +temp%10
        temp//=10
    return rev
    
n = int(input())
rn = REV(n)

if prime(n) and prime(rn):
    print('circular prime')
elif prime(n):
    print('prime but not a circular prime')
else:
    print('not prime')