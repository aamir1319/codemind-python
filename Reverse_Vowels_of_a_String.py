s = list(input())
n = []

z = ['a','e','i','o','u','A','E','I','O','U']

for i in s:
    if i in z:
        n.append(i)
n = n[::-1]
j = 0
for i in range(len(s)):
    if s[i] in z:
        s[i] = n[j]
        j+=1

for i in s:
    print(i,end='')