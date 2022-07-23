n = int(input())

arrA = list(map(int,input().split()))

sortarrA = sorted(arrA)
ans = [0 for _ in range(n)]
cnt = 0


for i in sortarrA:
    x = arrA.index(i)
    ans[x] = cnt
    arrA[x] = -1
    cnt += 1

for i in ans:
    print(i,end=" ")