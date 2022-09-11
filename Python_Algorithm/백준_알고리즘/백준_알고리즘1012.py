n = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(ly,lx):
    global cnt,chk
    q = [(ly,lx)]

    while q:
        ey,ex = q.pop()
        for l in range(4):
            nx = ex + dx[l]
            ny = ey + dy[l]

            if 0<=nx<x and 0<=ny<y:
                if nlist[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny,nx))


    return


for j in range(n):
    x, y, k = map(int, input().split())
    nlist = [[0 for _ in range(x)] for _ in range(y)]
    chk = [[False for _ in range(x)] for _ in range(y)]
    cnt=0
    rl=[]
    for i in range(k):
        x1,y1 = map(int, input().split())
        nlist[y1][x1] = 1


    for yy in range(y):
        for xx in range(x):
            if nlist[yy][xx] == 1 and chk[yy][xx] == False:
                chk[yy][xx] = True
                bfs(yy,xx)
                cnt+=1

    print(cnt)


