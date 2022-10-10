a = int(input())
sum,prod=0,1
while a:
    sum+=a%10
    prod*=a%10
    a//=10
print(prod-sum)