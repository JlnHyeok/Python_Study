### 버블 정렬의 구현

def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):   # 배열 크기-1번 반복, end변수 : 각 사이클의 끝 위치 지정
        for cur in range(0, end):   # 각 사이클의 맨 앞부터 end-1번째까지 반복
            if ary[cur] > ary[cur+1]:   # 현재(cur)와 현재 다음(cur+1)의 위치값을 비교
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]     # 두 값을 교환
    return ary

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
print('정렬 전 -->', dataAry)
dataAry = bubbleSort(dataAry)
print('정렬 후 -->', dataAry)