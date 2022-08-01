board = [[None for _ in range(7)] for _ in range(7)]

chess = []

for i in range(36):
    chess.append(input())


for i in range(1,7):
    for j in range(1,7):
        board[j][i] = chr(ord('A')+i-1)+str(7-j)

for i in range(1,7):
    for j in range(1,7):
        print(board[i][j], end=' ')
    print()

while 1:
    i=1
    a = chess.pop(0)
    for i in range(1,7):
        for j in range(1,7):
            if a == board[i][j]:
                print(a,i,j)
                a = chess.pop(0)

                if 3<=i<=4 and 3<=j<=4:
                    if a in (board[i-2][j+1],board[i-2][j-1],board[i-1][j+2], board[i+2][j+1],board[i+1][j+2],board[i+1][j-2],board[i+2][j-1],board[i-1][j-2]):
                        print('Valid')
                elif 2<=i<=5 and 2<=j<=5:
                    if i==2:
                        if j==3 or j==4:
                            if a in (board[i-1][j+2],board[i+2][j+1],board[i+1][j+2],board[i+1][j-2],board[i+2][j-1],board[i-1][j-2]):
                                print('Valid')
                        elif j==1:
                            if a in (board[i-1][j+2], board[i+2][j+1],board[i+1][j+2],board[i+2][j-1]):
                                print('Valid')
                        elif j==5:
                            if a in (board[i+2][j+1],board[i-1][j+2],board[i+1][j-2],board[i+2][j-1],board[i-1][j-2]):
                                print('Valid')
                        else:
                            print('Invalid')
                            exit()
                    elif 2<i<5:
                        if i==3 or i==4:
                            if j==2:
                                if a in (board[i-2][j+1],board[i-2][j-1],board[i-1][j+2], board[i+2][j+1],board[i+1][j+2],board[i+2][j-1]):
                                    print('Valid')
                            if j==5:
                                if a in (board[i-2][j+1],board[i-2][j-1],board[i+2][j+1],board[i+1][j-2],board[i+2][j-1],board[i-1][j-2]):
                                    print('Valid')
                            else:
                                print('Invalid')
                                exit()
                    elif i==5:
                        if j==2:
                            if a in (board[i-2][j+1],board[i-2][j-1],board[i-1][j+2],board[i+1][j+2],board[i-1][j-2]):
                                print('Valid')
                        elif j==3 or j==4:
                            if a in (board[i-1][j+2],board[i-2][j+1],board[i-2][j-1], board[i+2][j+1],board[i+1][j+2],board[i+1][j-2],board[i-1][j-2]):
                                print('Valid')
                        elif j==5:
                            if a in (board[i-2][j+1],board[i-2][j-1],board[i+1][j-2],board[i-1][j-2]):
                                print('Valid')
                        else:
                            ('Invalid')
                else:
                    if i==1:
                        pass
                    if i==2:
                        pass
                    if i==3 or i==4:
                        pass
                    if i==5:
                        pass
                    if i==6:
                        pass