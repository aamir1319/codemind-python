a = list(map(int,input().split()))
b = list(map(int,input().split()))
score= [0,0]
for i in range(3):
    if a[i]==b[i]:
        pass
    elif a[i]>b[i]:
        score[0]+=1
    elif a[i]<b[i]:
        score[1]+=1
for i in score:
    print(i,end=' ')