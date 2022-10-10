n = int(input())

sq = n*n

temp = sq
sum_=0

while(temp>0):
    sum_+=temp%10
    temp//=10
if sum_==n:
    print('Neon Number')
else:
    print('Not Neon Number')