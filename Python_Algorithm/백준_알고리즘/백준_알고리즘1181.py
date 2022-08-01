n=int(input())
arr=[]
for i in range(n):
    str = input()
    if str in arr:
        continue
    else:
        arr.append(str)

# for k in range(len(arr)-1):
#     for j in range(k+1,len(arr)):
#         if len(arr[k])>len(arr[j]):
#             arr[k],arr[j] = arr[j],arr[k]
#
#         if len(arr[k])==len(arr[j]):
#             if arr[k]>arr[j]:
#                 arr[k], arr[j] = arr[j], arr[k]
arr = sorted(arr)           # --> 훨씬 시간 단축
arr = sorted(arr,key=len)
for i in arr:
    print(i)







# N=int(input()) # 입력받을 개수
# result=[] # 결과값 배열로 저장
#
# for i in range(0,N): # 개수만큼 입력받고 result에 저장
#     result.append(input())
#
# result=list(set(result)) # set을 이용해 중복 제거
# result.sort() # 알파벳 순으로 정렬
# result.sort(key=len) # 길이 순으로 정렬
#
# for i in result:
#     print(i)