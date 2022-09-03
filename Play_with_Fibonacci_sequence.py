n=int(input())
a=0
b=1
print(a,b,end=" ")
for i in range(n-2):
    print(a+b,end=" ")
    a,b=b,a+b