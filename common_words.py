s1= input().lower().split()
s2 = input().lower().split()
for i in s2:
    if i in s1:
        print(i,end=' ')