
n,m = map(int,input().split())

q = [0 for _ in range(n)]
cnt = 0
ans = list(map(int,input().split()))

for i in ans:
    q[i-1] = i

while ans:
    if ans[0] == q[0]:
        ans.pop(0)
        q.pop(0)
    else:
        idx = q.index(ans[0])
        if idx<=len(q)-idx-1:
            q.append(q.pop(0))
            cnt+=1
        else:
            q.insert(0,q.pop())
            cnt+=1

print(cnt)