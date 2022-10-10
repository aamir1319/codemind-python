def palin(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if n==rev:
        return True
    return False 
    
n=int(input())
after=n+1
before=n-1
while after:
    if palin(after):
        break
    after+=1
while before:
    if palin(before):
        break
    before-=1
diff=after-n
diff1=n-before
if diff>diff1:
    print(before)
elif diff==diff1:
    print(before,after)
else:
    print(after)