### 이미 정렬된 줄에 끼어들기

import random
import time

# 버블 정렬
def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        # 각 사이클마다 자리 바꿈이 발생되었는지 확인하는 변수 --> changeYN
        # 우선은 자리 바꿈이 발생되지 않았다고 가정
        changeYN = False
        print('# 사이클 ->', ary)  # 사이클이 몇번 수행되었는지 체크하려고 배열 상태 출력
        for cur in range(0, end):
            if  ary[cur] > ary[cur+1]:
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True     # 자리 바꿈이 발생하면 True로 변경
        if not changeYN:    # 자리바꿈이 일어나지 않았다면 이미 정렬이 완료된 것이므로
            break           # 반복문을 종료
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
tempAry = [random.randint(10000, 99999) for _ in range(1000000)]    # 임의의 데이터 백만개 생성
tempAry.sort()  # 파이썬의 정렬 기능을 이용해서 정렬

rndPos = random.randint(0, len(tempAry)-1)  # 끼어들 임의의 위치를 선정한다.
print('# 데이터 개수 ->', len(tempAry))
print('# 끼어든 위치 -->', rndPos)
tempAry.insert(rndPos, tempAry[-1])     # 이미 정렬된 배열에서 임의의 위치에 배열의 마지막 데이터를 끼워넣는다.

bubbleAry = tempAry[:]  # 버블 정렬할 배열 복사
quickAry = tempAry[:]   # 퀵 정렬할 배열 복사

start = time.time()     # 버블 정렬 시작 시간 설정
bubbleSort(bubbleAry)   # 버블 정렬 수행
end = time.time()       # 버블 정렬 끝 시간 설정
print(f'버블 정렬 시간 --> {end-start:8.3}초')

start = time.time()     # 퀵 정렬 시작 시간 설정
quickSort(quickAry)     # 퀵 정렬 수행
end = time.time()       # 퀵 정렬 끝 시간 설정
print(f'퀵 정렬 시간 --> {end-start:8.3f}초')