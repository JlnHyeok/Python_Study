T = int(input())


for j in range (T):
    x1 , y1, x2, y2 = map(int,input().split())

    N = int(input())
    count = 0

    for i in range(N):
        px,py,r = map(int,input().split())
        d1 = ((px-x1)**2 + (py-y1)**2)**0.5
        d2 = ((px-x2)**2 + (py-y2)**2)**0.5

        if d1<r or d2<r:
            if d1<r and d2<r:
                pass
            else:
                count+=1
    print(count)
