n = int(input())
b = bin(n).replace('0b','')
b = list(b)
# print(b)
for i in range(len(b)):
    if b[i]=='1':
        b[i]='0'
    else:
        b[i]='1'
# print(b)

pw= len(b)-1
s = 0
for i in b:
    s+= int(i)*(2**pw)
    pw-=1
print(s)