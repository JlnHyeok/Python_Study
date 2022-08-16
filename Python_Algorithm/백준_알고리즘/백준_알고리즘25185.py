n = int(input())

card = [[None for _ in range(4)] for _ in range(n)]

for i in range(n):
    card[i] = input().split()
    card[i] = list(sorted(set(card[i])))

for i in range(n):
    if len(card[i])<3:
        print(':)')
    elif len(card[i]) == 3:
        if (int(card[i][0][0]) + 2 == int(card[i][1][0]) + 1 == int(card[i][2][0])) and \
                card[i][0][1] == card[i][1][1] == card[i][2][1]:
            print(':)')
        else:
            print(':(')
    elif len(card[i]) == 4:
        cnt = 0
        if (int(card[i][0][0]) + 2 == int(card[i][1][0]) + 1 == int(card[i][2][0])) and \
                (card[i][0][1]==card[i][1][1]==card[i][2][1]):
            cnt+=1
        if (int(card[i][0][0]) + 2 == int(card[i][1][0]) + 1 == int(card[i][3][0])) and \
                (card[i][0][1]==card[i][1][1]==card[i][3][1]):
            cnt+=1
        if (int(card[i][0][0]) + 2 == int(card[i][2][0]) + 1 == int(card[i][3][0])) and \
                (card[i][0][1]==card[i][2][1]==card[i][3][1]):
                cnt+=1
        if (int(card[i][1][0]) + 2 == int(card[i][2][0]) + 1 == int(card[i][3][0])) and \
                (card[i][1][1] == card[i][2][1] == card[i][3][1]):
            cnt += 1
        if cnt>=1:
            print(':)')
        else:
            print(':(')