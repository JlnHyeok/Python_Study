s = input()
cnt = 0
while s:
    if s[0] == '0':
        s = s.lstrip('0')
        cnt+=1
    else:
        s = s.lstrip('1')
        cnt+=1

if cnt%2 == 1:
    print(int((cnt-1)/2))
else:
    print(int(cnt/2))