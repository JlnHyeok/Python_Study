### 선택 정렬과 퀵 정렬의 성능 비교하기

import random
import time

# 선택 정렬
def selectionSort(ary):
    n = len(ary)    # 배열의 길이
    for i in range(0, n-1):     # 배열 크기-1 횟수만큼 반복
        minIdx = i
        for k in range(i+1, n):
            if ary[minIdx] > ary[k]:
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]   # 0번째 값과 찾은 최소값을 교환
    return ary

# 퀵 정렬
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

## 메인 코드 부분
countAry = [1000, 10000, 12000, 15000]  # 임의로 생성할 데이터 개수를 배열에 미리 저장

for count in countAry:
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]  # 선택 정렬 배열에 복사
    quickAry = tempAry[:]   # 퀵 정렬 배열에 복사

    print('## 데이터 수 :', count, '개')
    start = time.time()     # 선택 정렬 시작 시간 설정
    selectionSort(selectAry)    # 선택 정렬 수행
    end = time.time()       # 선택 정렬 끝 시간 설정
    print(f'선택 정렬 --> {end-start:8.3f}초')   # 걸린 시간을 초 단위로 출력

    start = time.time()
    quickSort(quickAry)
    end = time.time()
    print(f'퀵 정렬 --> {end-start:8.3f}초')