s = input().lower().replace(' ','')
s1 = input().lower()

temp = []
for i in s:
    if i not in temp and i in s1:
        temp.append(i)
for i in sorted(temp):
    print(i,end='')
if len(temp)==0:
    print(-1)