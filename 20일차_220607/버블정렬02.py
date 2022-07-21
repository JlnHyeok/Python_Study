### 개선된 버블 정렬의 구현

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

dataAry = [50, 105, 120, 188, 150, 162, 168, 177]
print('정렬 전 -->', dataAry)
dataAry = bubbleSort(dataAry)
print('정렬 후 -->', dataAry)