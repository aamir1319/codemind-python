def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
n1=int(input())
n2=int(input())
k=n1+n2
for i in range(1,10000):
    if prime(i+k):
        print(i)
        break