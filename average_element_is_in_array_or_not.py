n=int(input())
x=list(map(int,input().split()))
s=sum(x)
avg=s//n
for i  in x:
    if avg in x:
        print(True)
        break
else:
    print(False)