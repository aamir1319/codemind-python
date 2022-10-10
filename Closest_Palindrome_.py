n = int(input())

after = n+1
before = n-1

while after:
    temp = after
    rev =0 
    while temp>0:
        rev = rev*10 + temp%10
        temp//=10
    if rev==after:
        break
    after+=1

while before:
    temp = before
    rev = 0
    while temp>0:
        rev = rev*10 + temp%10
        temp//=10
    if rev == before:
        break
    before-=1
    
if (n-before)>(after-n):
    print(after)
elif (n-before)==(after-n):
    print(before,after)
else:
    print(before)