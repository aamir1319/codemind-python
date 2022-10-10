def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    after = n
    before =n
    while after:
        if prime(after):
            break
        after+=1
    
    while before:
        if prime(before):
            break
        before-=1
    
    daf = after-n
    dbef  = n-before
    
    if daf==dbef:
        print(before)
    elif daf>dbef:
        print(before)
    else:
        print(after)