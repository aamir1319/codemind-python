num,d = map(int,input().split())
num = list(str(num))
sum_front = 0
sum_back = 0
for i in range(d):
    sum_front =sum_front *10 + int(num[i])
for i in range(d,0,-1):
    sum_back = sum_back*10 + int(num[-i])
print(abs(sum_front-sum_back))