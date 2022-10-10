a = list(map(int,input()))

for i in range(len(a)):
    flag=1
    for j in range(len(a)):
        if i==j:
            continue
        else:
            if a[i]==a[j]:
                flag=0
                break
    if flag==0:
        break
if flag==1:
    print('Unique Number')
else:
    print('Not Unique Number')