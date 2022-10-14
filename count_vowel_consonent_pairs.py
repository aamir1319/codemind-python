s = input()
v = 'aeiouAEIOU'
c=0
# print(s)
for j in range(len(s)//2):
    if s[j]==' ' or s[-(j+1)]==' ':
        continue
    if (s[j] in v and s[-(j+1)] not in v) or (s[j] not in v and s[-(j+1)] in v):
        c+=1
print(c)