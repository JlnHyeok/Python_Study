x,y = map(int,input().split())
z = 100*y//x
start = 0
end = 2000000000
ans = 1
if z>=99:
    print(-1)
else:
    while start <= end:
        mid = (start+end)//2
        if ((y+mid)*100)//(x+mid)>z:
            end = mid -1
        else:
            start = mid+1
    print(start)