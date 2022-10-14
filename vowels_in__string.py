s = input()
v = 'aeiouAEIOU'
c=0
temp = []
for  i in s:
    if i in v and i not  in temp:
        print(i,end=' ')
        temp.append(i)
        c=1
if c==0:
    print(-1)