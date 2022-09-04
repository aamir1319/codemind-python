h,spi,s=map(int,input().split())
if ((h>50) and (spi>60)and (s>100)):
    print("10")
elif((h>50) and (spi>60)):
    print("9")
elif((spi>60) and (s>100)):
    print("8")
elif((h>50) and (s>100)):
    print("7")
elif((h>50) or (spi>60) or (s>100)):
    print("6")
else:
    print("5")
    