a = int(input())
negative =0
if a<0:
    negative=1
    a*=-1
temp = a
rev = 0

while(temp>0):
    rev = rev*10+temp%10
    temp//=10
if negative==1:
    rev*=-1
print(rev)