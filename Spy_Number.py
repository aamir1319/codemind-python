a = int(input())

sum_=0
prod =1

temp =a
while(temp>0):
    sum_+= temp%10
    prod*=temp%10
    temp//=10
if sum_==prod:
    print('Spy Number')
else:
    print('Not Spy Number')