s = input().split()
v = 'aeiou'
mc = 0
for i in s[0]:
    if i in v:
        mc+=1

for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    if mc>c:
        mc = c

print(mc)