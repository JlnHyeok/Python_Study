import sys
input = sys.stdin.readline
n=int(input())
arr = list(map(int , input().split()))

ans = [0 for _ in range(n)]
ans[0] = arr[0]

for i in range(1,n):
    ans[i] = max(arr[i]+ans[i-1] ,arr[i])

print(max(ans))

# 처음 풀이
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         ans = sum(arr[i:j+1])
#         if first<ans:
#             first=ans
#
# print(first)
