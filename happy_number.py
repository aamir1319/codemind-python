n=int(input())
while True:
    s=0
    c=0
    while n!=0:
        rem=n%10
        n//=10
        s+=rem*rem
        c+=1
    n=s
    if c==1:
        if s==1 or s==7:
            print(True)
            break
        else:
            print(False)
            break