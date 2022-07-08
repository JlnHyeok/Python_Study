### 정렬되지 않은 데이터의 순차 검색

def seqSearch(ary, fData):
    pos = -1    # 찾는 위치, 이 값이 변경되지 않으면 찾지 못한 것
    size = len(ary)
    print('## 비교한 데이터 -->', end=' ')
    for i in range(size):   # 배열의 처음부터 끝까지 찾는 값(fData)와 비교
        print(ary[i], end=' ')
        if ary[i] == fData:     # 데이터를 찾으면
            pos = i             # 찾은 위치를 저장하고 반복문 종료
            break
    print()
    return pos  # 찾은 위치를 반환

findData = int(input('찾을 값을 입력하세요 -->'))
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1:
    print(findData,'이(가) 없네요.')
else:
    print(f'{findData}은(는) {position}위치에 있음')
