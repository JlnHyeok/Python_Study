n = int(input())

c = 0

n_list = [[None for _ in range(n)] for _ in range(n)]

for i in range(n):
    n_list[i] = list(input())

for i in range(n):
    ans = [None for _ in range(n)]
    for j in range(n):
        if n_list[i][j] == 'Y':
            ans[j] ='Y'
            for k in range(n):
                if n_list[j][k] == 'Y' or (n_list[j][k] == 'N' and ans[k]=='Y'):
                    if k==i:
                        continue
                    ans[k] = 'Y'
                else:
                    ans[k] ='N'
    if ans.count('Y')>c:
        c = ans.count('Y')

print(c)
