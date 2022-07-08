### 재귀 호출 함수 기본 ###

def openBox():
    print('종이 상자를 엽니다!!')
    openBox()  # 함수 자신을 호출

openBox()  # 함수를 처음 호출

