import sys
input = sys.stdin.readline
# 리스트보다 set이 연산속도가 더 빠르다
n=int(input())
w,h = map(int,input().split())
pl =set(tuple(map(int,input().split())) for _ in range(n))

cnt = 0
# x = -200000000
# y = -200000000
# for i in range(n-1):
#     ans = []
#     ans.append(pl[i])
#     chw=0
#     chy=0
#     j=i+1
#     while j<n:
#         if abs(pl[i][0] - pl[j][0]) == w and pl[i][1]==pl[j][1]:
#             if chw<1:
#                 chw+=1
#                 ans.append(pl[j])
#                 x=pl[j][0]
#         if abs(pl[i][1] - pl[j][1]) == h and pl[i][0] == pl[j][0]:
#             if chy<1:
#                 chy+=1
#                 ans.append(pl[j])
#                 y=pl[j][1]
#         if chw == 1 and chy == 1:
#             break
#         j+=1
#
#     if [x,y] in pl:
#         if [x,y] not in ans:
#             ans.append([x,y])
#
#     if len(ans) == 4:
#        cnt+=1

for a,b in pl:
    if (a + w , b) in pl and (a,b+h) in pl and (a+w,b+h) in pl:
        cnt+=1

print(cnt)
