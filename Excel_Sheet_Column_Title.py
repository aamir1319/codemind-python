n = int(input())
a = [chr(i) for i in range(65,91)]
# print(a)

temp = n
s = ''
while temp:
    temp-=1
    s+=a[temp%26]
    temp//=26
print(s[::-1])