n=int(input())
while True:
    p=0
    while n:
        p+=n%10
        n//=10
    if len(str(p))==1:
        print(p)
        break
    else:
        n=p