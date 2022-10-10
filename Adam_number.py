n=int(input())
sq=n*n
# print(sq)
temp=n
rev=0
while temp:
    rev=rev*10+temp%10
    temp//=10
    
sqq=rev*rev
revv=0
temp=sqq
while temp:
    revv=revv*10+temp%10
    temp//=10
# print(sqq)
if sq==revv:
    print("True")
else:
    print("False")