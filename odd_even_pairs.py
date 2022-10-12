n = int(input())
x = list(map(int,input().split()))

e=[]
o = []
for i in x:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
for i in range(max(len(e),len(o))):
    if len(e)==0:
        print(o[0],end=' ')
        o.remove(o[0])
    elif len(o)==0:
        print(e[0],end=' ')
        e.remove(e[0])
    elif len(e)!=0 and len(o)!=0:
        print(o[0],e[0],end=' ')
        e.remove(e[0])
        o.remove(o[0])
    else:
        break
if n%2!=0:
    print(0)