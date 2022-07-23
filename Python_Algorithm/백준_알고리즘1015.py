n = int(input())

arrA = list(map(int,input().split()))

sortarrA = sorted(arrA)
ans = [0 for _ in range(n)]
cnt = 0


for i in sortarrA:
    x = arrA.index(i)   # i값의 인덱스를 구한다.
    ans[x] = cnt
    arrA[x] = -1        # 즁복 방지를 위해 음수로지정
    cnt += 1

for i in ans:
    print(i,end=" ")