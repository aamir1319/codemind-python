s = list(input())
flag=0
for i in range(len(s)):
    for j in range(len(s)):
        if i==j:
            continue
        if s[i]==s[j]:
            flag=0
            break
        else:
            flag=1
    if flag==1:
        print(i)
        break
    else:
        continue
if flag==0:
    print(-1)