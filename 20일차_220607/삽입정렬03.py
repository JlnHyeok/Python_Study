### 삽입 정렬의 효율적인 구현

def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):     # end변수 : 각 사이클의 끝 위치를 지정
        for cur in range(end, 0, -1):   # 맨 뒤부터 1번째까지 반복
            if ary[cur-1] > ary[cur]:   # 현재(cur)와 현재 앞(cur-1)의 위치 값을 비교
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]     # 두 값을 교환
    return ary

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
print('정렬 전 -->', dataAry)
dataAry = insertionSort(dataAry)
print('정렬 후 -->', dataAry)