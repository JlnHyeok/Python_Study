### 배열에서 자신이 삽입 될 위치를 찾는 함수

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

testAry = []
insPos = findInsertIdx(testAry, 55)     # 빈 배열에 55를 삽입
print('삽입할 위치 -->', insPos)

testAry = [33, 77, 88]
insPos = findInsertIdx(testAry, 55)     # 중간에 55를 삽입
print('삽입할 위치 -->', insPos)

testAry = [33, 55, 77, 88]
insPos = findInsertIdx(testAry, 100)    # 자신보다 큰 값이 없을때
print('삽입할 위치 -->', insPos)