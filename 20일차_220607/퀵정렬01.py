### 퀵 정렬의 간단한 구현

def quickSort(ary):
    n = len(ary)
    if n <= 1:      # 정렬할 리스트의 개수가 1개 이하라면
        return ary  # 이미 정렬된 배열이다.
    pivot = ary[n // 2]     # 기준 값을 중간값으로 지정
    # 기준보다 작은 데이터를 저장할 왼쪽 배열, 기준보다 큰 데이터를 저장할 오른쪽 배열을 준비
    leftAry, rightAry = [], []
    for num in ary:
        if num < pivot:     # 기준에 따라 왼쪽, 오른쪽 배열에 데이터 저장
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
    return quickSort(leftAry) + [pivot] + quickSort(rightAry)   # 재귀호출해서 정렬한 후 반환

dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)