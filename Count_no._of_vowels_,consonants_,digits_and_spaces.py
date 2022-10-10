s= input().lower()

vcount = 0
ccount = 0
dcount = 0
wcount = 0
v = ['a','e','i','o','u']
for i in s:
    if i in v:
        vcount+=1
    elif i==' ':
        wcount+=1
    elif i.isdigit():
        dcount+=1
    else:
        ccount+=1
        
print('Vowels:',vcount)
print('Consonants:',ccount)
print('Digits:',dcount)
print('White spaces:',wcount)