s= input().split()

maxc = 0
for i in s:
    if len(i)>maxc:
        maxc = len(i)
        
print(maxc)