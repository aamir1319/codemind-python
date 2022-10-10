n = int(input())

x= list(map(int,input().split())) 
max_,el = 0, 0

for i in x:
    if x.count(i)>abs (n/2):
        print(i)
        break