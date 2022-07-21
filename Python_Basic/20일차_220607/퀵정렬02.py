### 퀵 정렬의 간단한 구현(중복된 값을 고려)

def quickSort(ary):
    n = len(ary)
    if n <= 1:
        return ary
    pivot = ary[n // 2]     # 중간값
    # 기준과 동일한 데이터가 있을 경우에 저장할 midAry를 준비한다.
    # midAry에는 모두 동일한 값이 들어간다.
    leftAry, midAry, rightAry = [],[],[]
    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
        else:
            midAry.append(num)  # 기준과 동일한 데이터는 midAry에 저장
    return quickSort(leftAry) + midAry + quickSort(rightAry)

dataAry = [120, 120, 188, 150, 168, 50, 50, 162, 105, 120, 177, 50]
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)