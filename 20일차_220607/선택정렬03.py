### 개선된 선택 정렬

def selectionSort(ary):
    n = len(ary)    # 배열의 길이
    for i in range(0, n-1):     # 배열 크기-1 횟수만큼 반복
        minIdx = i
        for k in range(i+1, n):
            if ary[minIdx] > ary[k]:
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]   # 0번째 값과 찾은 최소값을 교환
    return ary

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)