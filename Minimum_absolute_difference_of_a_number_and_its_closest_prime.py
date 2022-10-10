def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if  n%i==0:
            return False
    return True

a = int(input())
after = a
before =a
while after:
    
    if prime(after):
        break
    after+=1

while before:
    if prime(before):
        break
    before-=1
    
if (after-a)>(a-before):
    print(abs(a-before))
else:
    print(abs(a-after))
    