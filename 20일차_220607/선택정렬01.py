### 배열에서 최소값의 위치를 찾는 함수

def findMinIdx(ary):
    minIdx = 0  # 배열의 첫번째 값(0번째 값)을 현재 최소값 위치로 지정
    for i in range(1, len(ary)):    # 배열의 두번째 값(1번 인덱스)부터 마지막까지 반복
        if ary[minIdx] > ary[i]:    # 배열의 i번째 값과 현재 최소값을 비교해서
            minIdx = i              # i번째 값이 더 작으면 i를 현재 최솟값 위치로 지정
    return minIdx   # 찾아낸 배열의 최소값 위치를 반환

testAry = [55, 88, 33, 77]
minPos = findMinIdx(testAry)
print(' 최솟값 -->', testAry[minPos])