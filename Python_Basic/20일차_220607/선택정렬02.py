### 선택 정렬의 구현

## 함수 선언 부분
def findMinIdx(ary):
    minIdx = 0  # 배열의 첫번째 값(0번째 값)을 현재 최소값 위치로 지정
    for i in range(1, len(ary)):    # 배열의 두번째 값(1번 인덱스)부터 마지막까지 반복
        if ary[minIdx] > ary[i]:    # 배열의 i번째 값과 현재 최소값을 비교해서
            minIdx = i              # i번째 값이 더 작으면 i를 현재 최솟값 위치로 지정
    return minIdx   # 찾아낸 배열의 최소값 위치를 반환

## 전역 변수 선언 부분
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분
print('정렬 전 -->', before)
for _ in range(len(before)):    # 배열의 크기만큼 반복을 하겠다
    minPos = findMinIdx(before)     # 정렬 전 배열에서 최소값의 위치를 찾고
    after.append(before[minPos])    # 정렬 후 배열의 맨 뒤에 추가
    # 정렬 후 배열에 넣은 값을 정렬 전 배열에서 제거
    # 이제 정렬 전 배열에는 가장 작은 값을 제외한 나머지 데이터만 남는다.
    del(before[minPos])
print('정렬 후 -->', after)