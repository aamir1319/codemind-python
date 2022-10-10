n = int(input())
s = list(map(str,input().split()))
a = ''
for i in s:
    a+=i

b = int(a)

b+=1

a = list(str(b))

for i in a:
    print(i,end=' ')