n,m = map(int,input().split())

board = [[None for _ in range(n)] for _ in range(m)]
diff=[None for _ in range((n-7)*(m-7))]
cnt = 0
l = 0
cc = 0
for i in range(n):
    board[i] = list(input())


for j in range(n-7):

    for k in range(n):
        cnt = 0
        cc = 0
        for i in range(m-1):
            if cc>7:
                break
            if board[j+k][i]==board[j+k][i+1]:
                cnt+=1
            cc+=1

print(diff)