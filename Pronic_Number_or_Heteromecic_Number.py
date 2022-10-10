a = int(input())
flag=0
for i in range(1,a):
    if i*(i+1)==a:
        flag=1
        break
if flag==1:
    print('YES')
else:
    print('NO')