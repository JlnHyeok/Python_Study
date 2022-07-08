### 반환 조건을 추가한 재귀 호출 함수 ###

count = 10   # 전역 변수

def openBox():
    global count
    print('종이 상자를 엽니다!!')
    count -= 1
    if count == 0:
        print('** 반지를 넣고 반환합니다! **')
        return
    openBox()  # 재귀 호출
    print('종이 상자를 닫습니다!!')

openBox()  # 함수 호출
