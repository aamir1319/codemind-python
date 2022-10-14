s = input().lower().replace(' ','')
s2 = input().lower()

temp = []
c=0
for i in s:
    if i not in temp and i in s2:
        temp.append(i)
        c+=1
print(c)