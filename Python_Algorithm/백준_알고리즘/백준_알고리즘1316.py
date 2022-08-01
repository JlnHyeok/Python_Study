N = int(input())
str = [None for _ in range(N)]

compare = [[None for _ in range(N)] for _ in range(N)]
cnt = 0

for i in range(N):
    str[i]=input()

for i in range(N):
    for j in range(len(str[i])-1):
        if str[i][j] != str[i][j+1]:
            if str[i][j] in str[i][j+1:]:
                cnt+=1
                break

# for i in range(len(compare)):
#     for j in range(len(compare[i])-1):
#         if compare[i][j] != compare[i][j+1]:
#             if compare[i][j] in compare[i][j+1:]:
#                 cnt+=1
#                 break

print(N-cnt)


# a = 'badrrabrv'
#
# print(list(a))
#
# print(sorted(a,key=a.find)) # 입력된 문자열 순으로 정렬인듯 하다
#
# print(list(a)==sorted(a,key=a.find))
#
# print(a.index) <-- a.find 랑 같은결과