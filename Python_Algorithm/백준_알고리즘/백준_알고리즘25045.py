n,m = map(int,input().split())
a = [None for _ in range(n)]
b = [None for _ in range(m)]
a = sorted(list(map(int,input().split())),reverse=True)
b = sorted(list(map(int,input().split())))

ans = 0

if n>=m:
    for i in range(m):
        if a[i]>=b[i]:
            ans += a[i]-b[i]
else:
    for i in range(n):
        if a[i]>=b[i]:
            ans += a[i]-b[i]

print(ans)
