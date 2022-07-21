### 정렬된 데이터의 이진 검색

def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary)-1

    while start <= end:     # 시작이 끝보다 커질때까지 반복
        mid = (start +end)//2   # 배열의 중앙 위치
        if fData == ary[mid]:   # 중앙 위치가 찾는 값이면 검색 성공
            return mid
        elif fData > ary[mid]:  # 찾는 값이 중앙 위치보다 크다면
            start = mid + 1     # 배열의 오른쪽에 존재, 시작점을 중앙 위치+1로 변경
        else:   # 찾는 값이 더 중앙 위치보다 작다면
            end = mid - 1       # 배열의 왼쪽에 존재, 끝점을 중앙 위치-1로 변경
    return pos

dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162  # 찾을 키

print('배열 -->', dataAry)
position = binSearch(dataAry, findData)

if position == -1:  # 배열에 찾는 값이 없을 경우
    print(findData,'이(가) 없네요')
else:
    print(f'{findData}는(은) {position}위치에 있음')
