import datetime

today = list(map(int,input().split()))
d_day = list(map(int,input().split()))


# a=''.join(today)    # ''.join(리스트) -> 문자열을 묶어줌

a = datetime.datetime(today[0],today[1],today[2])
b = datetime.datetime(d_day[0],d_day[1],d_day[2])

if d_day[0]-today[0]>=1000 and (d_day[1]>=today[1] and d_day[2]>=today[2]):
    print('gg')
    exit()
elif d_day[0]-today[0]>1000:
    print('gg')
    exit()
print(f'D-{(b-a).days}')

