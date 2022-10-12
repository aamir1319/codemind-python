for i in range(int(input())):
    s = input()
    for i in range(len(s)):
        if s[i]=='0':
            if i==0:
                print('0',end='')
            else:
                print('000',end='')
        elif s[i]=='1':
            if i==0:
                print('1',end='')
            else:
                print('001',end='')
        elif s[i]=='2':
            if i==0:
                print('10',end='')
            else:
                print('010',end='')
        elif s[i]=='3':
            if i==0:
                print('11',end='')
            else:
                print('011',end='')
        elif s[i]=='4':
            print('100',end='')
        elif s[i]=='5':
            print('101',end='')
        elif s[i]=='6':
            print('110',end='')
        elif s[i]=='7':
            print('111',end='')
    print()