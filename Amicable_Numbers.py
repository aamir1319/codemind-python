n=int(input())
m=int(input())
s=0
d=0
for i in range(1,n):
    if n%i==0:
        s+=i
for i in range(1,m):
    if m%i==0:
        d+=i
if s==m and d==n:
    print("Amicable")
else:
    print("Not Amicable")