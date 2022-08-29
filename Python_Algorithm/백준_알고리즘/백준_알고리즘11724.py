n,m = map(int,input().split())
li = [[0 for _ in range(n)] for _ in range(n)]
chk = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    x-=1
    y-=1
    li[y][x] = 1
    li[x][y] = 1

cnt = 0
o = [0 for _ in range(n)]
for i in range(n):
    o[i] = i

print(o)
while o:
    j=o.pop(0)
    yl = []
    for i in range(n):
        if li[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            chk[i][j] = True
            yl.append(i)
    print(yl)
    while yl:
        k = yl.pop(0)
        o.remove(k)
        for q in range(n):
            if li[k][q] == 1 and chk[k][q] == False:
                chk[k][q] = True
                chk[q][k] = True
                yl.append(q)
        if not yl:
            cnt+=1
print(chk)
print(cnt)