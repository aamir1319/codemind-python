s1 = input().lower().split()
s2= input().lower().split()

c=0
for i in s1:
    for j in s2:
        if i==j and s1.count(i)==1 and s2.count(j)==1:
            c+=1
print(c)