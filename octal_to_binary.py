n=input()
for i in range(len(n)):
    if n[i]=='0':
        if i==0:
            print('0')
        else:
            print('000',end='')
    elif n[i]=='1':
        if i==0:
            print('1',end='')
        else:
            print('001',end='')
    elif n[i]=='2':
        if i==0:
            print('10',end='')
        else:    
            print('010',end='')
    elif n[i]=='3':
        if i==0:
            print('11',end='')
        else:    
            print('011',end='')
    elif n[i]=='4':
        print('100',end='')
    elif n[i]=='5':
        print('101',end='')
    elif n[i]=='6':
        print('110',end='')
    elif n[i]=='7':
        print('111',end='')
    
