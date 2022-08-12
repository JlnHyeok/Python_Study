n = int(input())

ans = [None for _ in range(n)]

for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d1 = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
    if d1 == 0:
        if r1==r2:
            ans[i] = -1
        else:
            ans[i] = 0
    else:
        if d1 > r1+r2:
            ans[i] = 0
        elif d1 == r1 + r2 or d1 == abs(r1-r2):
            ans[i] = 1
        elif d1 < r1+r2:
            ans[i] = 2
            if d1 < abs(r1-r2):
                ans[i] = 0

for i in ans:
    print(i)



    # if d1 == r1+r2 or d1 == abs(r1-r2):
    #     ans[i] = 1
    # elif d1 < r1+r2:
    #     ans[i] = 2
    #     if x1 == x2 and y1 == y2:
    #         if r1 == r2:
    #             ans[i] = -1
    #         else:
    #             ans[i] = 0
    # elif d1 > r1+r2:
    #     ans[i] = 0
    # elif d1 <abs(r1-r2):
    #     ans[i] = 0

    # if ( x1==x2 and y1==y2 ) and r1==r2:
    #     ans[i] = -1
    # elif ( x1==x2 and y1==y2 ) and r1!=r2:
    #     ans[i] = 0
    # else:
    #     ans[i] = 2
    #     if d1 == (r1+r2) or d1 == abs(r1-r2):
    #         ans[i] = 1
    #     elif d1 > (r1 + r2) or d1 < abs(r1 - r2):
    #         ans[i] = 0
