n = int(input())
m = int(input())

fact1 =0
fact2 =0
for i in range(1,n):
    if n%i==0:
        fact1+=i
if fact1==m:
    for i in range(1,m):
        if m%i==0:
            fact2+=i
    if fact2==n:
        print('Amicable')
    else:
        print('Not Amicable')
else:
    print('Not Amicable')