s = input().lower()
c=0
temp=[]
for i in s:
    if s.count(i)==1 and i!=' ':
        c+=1
print(c)