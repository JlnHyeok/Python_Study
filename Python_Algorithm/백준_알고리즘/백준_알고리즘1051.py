n,m = map(int,input().split())

sq = [[None for _ in range(m)] for _ in range(n)]

for i in range(n):
    sq[i]=list(input())
l1 = 1
cnt1 = 1
wide =[1]
for i in range(len(sq)):
    for j in range(len(sq[i])-1):
        cnt1 = 1
        for k in range(j+1,len(sq[i])):
            if sq[i][j] !=sq[i][k]:
                cnt1+=1
            elif sq[i][j] == sq[i][k]:
                cnt1+=1
                l1 = cnt1
                if i+l1-1 <n:
                    if sq[i+l1-1][j] == sq[i][j] and sq[i+l1-1][k] == sq[i][j]:
                        wide.append(l1*l1)

print(max(wide))