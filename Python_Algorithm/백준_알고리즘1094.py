n = int(input())

arr=[64]
while sum(arr)!=n:
    cnt = 0
    arr[0]/=2
    arr.append(arr[0])
    for i in range(len(arr)-1):
        cnt+=arr[i]
    if cnt>=n:
        arr.pop()

print(len(arr))