n=input().lower().split()
c=0
for i in n:
    if i==i[::-1]:
        c+=1
print(c)        