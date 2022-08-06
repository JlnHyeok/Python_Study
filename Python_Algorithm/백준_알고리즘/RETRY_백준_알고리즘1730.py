n = int(input())

board = [[chr(46) for _ in range(n)] for _ in range(n)]

m = list(input())
a=b=0

def motion(x):
    global board,a,b

    if x =='D':
        try:
            if board[a][b] == chr(43):
                a+=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(45):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(124)
            elif board[a][b] == chr(45):
                board[a][b] = chr(43)
                a+=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(45):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(124)
            else:
                board[a][b] = chr(124)
                a+=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(45):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(124)
        except IndexError:
            a-=1

    elif x == 'R':
        try:
            if board[a][b] == chr(43):
                b+=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(124):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(45)
            elif board[a][b] == chr(124):
                board[a][b] = chr(43)
                b+=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(124):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(45)
            else:
                board[a][b] = chr(45)
                b+=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(124):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(45)
        except IndexError:
            b-=1

    elif x == 'U':
        try:
            if board[a][b] == chr(43):
                a-=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(45):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(124)
            elif board[a][b] == chr(45):
                board[a][b] = chr(43)
                a-=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(45):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(124)
            else:
                board[a][b] = chr(124)
                a-=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(45):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(124)
        except IndexError:
            a+=1

    elif x == 'L':
        try:
            if board[a][b] == chr(43):
                b-=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(124):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(45)
            elif board[a][b] == chr(124):
                board[a][b] = chr(43)
                b-=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(124):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(45)
            else:
                board[a][b] = chr(45)
                b-=1
                if board[a][b] == chr(43):
                    pass
                elif board[a][b] == chr(124):
                    board[a][b] = chr(43)
                else:
                    board[a][b] = chr(45)
        except IndexError:
            b+=1


for i in range(len(m)):
    motion(m[i])

for i in range(n):
    for j in range(n):
        print(board[i][j],end='')
    print()