n = input()

num_1 = 0
num_2 = 'ABC'
num_3 = 'DEF'
num_4 = 'GHI'
num_5 = 'JKL'
num_6 = 'MNO'
num_7 = 'PQRS'
num_8 = 'TUV'
num_9 = 'WXYZ'
num_0 = ''

cnt = 0
for i in n:
    if i in num_2:
        cnt+=3
    elif i in num_3:
        cnt+=4
    elif i in num_4:
        cnt+=5
    elif i in num_5:
        cnt+=6
    elif i in num_6:
        cnt+=7
    elif i in num_7:
        cnt+=8
    elif i in num_8:
        cnt+=9
    elif i in num_9:
        cnt+=10
print(cnt)