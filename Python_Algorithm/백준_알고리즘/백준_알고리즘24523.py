n = int(input())
n_list = [None for _ in range(n)]
n_list = list(map(int,input().split()))
f=-1
if n==1:
    print(-1)
    exit()
for i in range(n-1):
    cnt = 1
    if i<f:
        continue
    for j in range(i+1,n):
        if n_list[i] == n_list[j]:
            cnt+=1
        elif n_list[i] != n_list[j]:
            for k in range(cnt):
                print(j+1,end=' ')
            f=j
            break
        if i+cnt>n-1:
            for k in range(cnt):
                print(-1,end=' ')
            f=i+cnt

    if i+cnt == n-1:
        print(-1,end='')


     # cnt = n_list[i:].count(n_list[i])
     # # print(i)
     # for j in range(i+1,i+cnt):
     #     if n_list[i] != n_list[j]:
     #         print(j+1,end=' ')
     #         i=j
     #         break
     #     elif n_list[i] == n_list[j]:
     #         if j == i+cnt-1 and j<n-1:
     #            for k in range(cnt):
     #                print(i+cnt+1,end=' ')
     #            i += cnt
     #         if j == i+cnt-1 and j>=n-1:
     #            for k in range(cnt):
     #                print(-1,end=' ')
     #            i+=cnt
