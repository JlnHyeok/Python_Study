n = list((input()))

# print(n)
k=0
a = []
if len(n)==1:
    print(0)
    if int(n[0]) % 3 == 0:
        print('YES')
    else:
        print('NO')
    exit()
else:
    while len(n)>1:
        for i in range(len(n)):
            k+=int(n[i])
        n = list(str(k))
        a.append(k)
        k=0

# print(a)

print(len(a))

if a[-1]%3 ==0:
    print('YES')
else:
    print('NO')