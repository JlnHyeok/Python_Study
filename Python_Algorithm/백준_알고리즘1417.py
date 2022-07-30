n = int(input())
c = [None for _ in range(n)]
cnt = 0
for i in range(n):
    c[i] = int(input())

if max(c) == c[0]:
    if c[0] in c[1:]:
        cnt+=1
        print(cnt)
        exit()
else:
    while 1:
        c[c.index(max(c))] -= 1
        c[0]+=1
        cnt+=1
        if max(c)==c[0]:
            if c[0] in c[1:]:
                cnt+=1
                break
            else:
                break
print(cnt)