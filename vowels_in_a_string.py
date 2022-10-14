s = input()
k = input()

for i in range(len(s)):
    if s[i]==k:
        print(True)
        print(i)
        break
else:
    print(False)