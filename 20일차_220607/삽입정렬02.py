### 삽입 정렬의 구현

def findInsertIdx(ary, data):   # ary : 배열 / data : 삽입 될 값
    findIdx = -1    # 초기값은 없는 위치로
    for i in range(0, len(ary)):
        if ary[i] > data:   # 배열에서 자신보다 큰 값을 찾으면
            findIdx = i     # 그 위치가 삽일될 위치
            break
    if findIdx == -1:   # 큰 값을 못찾은 경우 --> 제일 마지막에 위치
        return len(ary)
    else:
        return findIdx

before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

print('정렬 전 -->', before)
for i in range(len(before)):
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)  # insPos번 자리에 data를 넣는다.
print('정렬 후 -->', after)