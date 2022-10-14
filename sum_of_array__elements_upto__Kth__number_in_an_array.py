n = int(input())
x = list(map(int,input().split()))
k = int(input())
s=0
for i in x:
   s+=i
   if i==k:
       break
print(s)