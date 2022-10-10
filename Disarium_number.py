n = int(input())

temp =n
count=0
while temp>0:
    count+=1
    temp//=10
sum=0
temp=n
while temp>0:
    sum+= (temp%10) ** count
    count-=1
    temp//=10
print(sum==n)