def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
    
t=int(input())
for i in range(t):
    n=int(input())
    if prime(n):
        print(n)
    else:
        after=n+1
        before=n-1
        while after:
            if prime(after):
                break
            after+=1
        while before:
            if prime(before):
                break
            before-=1
        diff=after-n
        diff1=n-before
        if diff>diff1:
            print(before)
        elif diff==diff1:
            print(before)
        else:
            print(after)