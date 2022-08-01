ans=[]
while 1:
    n = int(input())
    if n == 0:
        break
    str = [None for _ in range(n+1)]
    str_dict = {}

    num = []
    memo = []
    for i in range(1,n+1):
        str[i] = input()
        str_dict[i] = str[i]
    for i in range(1,2*n):
        memo = list(input().split())
        memo[0] = int(memo[0])
        if memo[0] in num:
            num.remove(memo[0])
        else:
            num.append(memo[0])

    for i in num:
        ans.append(str_dict[i])

for i in range(len(ans)):
    print((i+1),ans[i])