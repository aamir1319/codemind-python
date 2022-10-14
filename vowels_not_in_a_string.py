s = input()
v = 'aeiou'
temp = []
for i in v:
    if i not in s:
        temp.append(i)
for i in sorted(temp):
    print(i,end=' ')
if len(temp)==0:
    print(0)