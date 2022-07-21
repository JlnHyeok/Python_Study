### 스택 동작을 위한 일반 코드

## 전역 변수 선언

SIZE = int(input('스택 크기를 입력하세요 --> '))
stack = [None for _ in range(SIZE)]
top = -1

## 스택이 꽉 찼는지 확인하는 함수

def isStackFull():
    if top >= SIZE -1:  # top이 스택크기 -1과 같으면 맨 끝이고, 스택이 꽉 찬 것이므로
        return True     # 참을 리턴한다
    else:
        return False

## 스택이 비었는지 확인하는 함수

def isStackEmpty():
    if top == -1: # 스택이 빈 경우
        return True
    else:
        return False

## 스택에 데이터를 삽입하는 함수

def push(data):
    global stack, top
    if isStackFull():
        print('스택이 꽉 찼습니다.')
        return
    top += 1
    stack[top] = data   # 데이터 삽입

## 스택에서 데이터를 추출하는 함수

def pop():
    global stack, top
    if isStackEmpty():
        print('스택이 비었습니다.')
        return None
    data = stack[top]   # 데이터를 추출하고
    stack[top] = None   # 그 자리에 None을 대입하고 삭제
    top -= 1
    return data         # 추출한 데이터를 반환

## 스택에서 top 위치의 데이터를 확인하는 함수

def peek():
    if isStackEmpty():
        print('스택이 비었습니다.')
        return None
    return stack[top] # 현재 top위치의 데이터를 반환

## 메인 코드 부분

if __name__ == '__main__':
    while 1:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 --> ')
        if select == 'I' or select == 'i':
            data = input('입력할 데이터 --> ')
            push(data)   # 삽입 함수 호출
            print('스택 상태 :', stack)

        elif select == 'E' or select == 'e':
            data = pop()    # 추출 함수 호출
            print('추출된 데이터 -->', data)
            print('스택 상태 :', stack)

        elif select == 'V' or select == 'v':
            data = peek()   # 확인 함수 호출
            print('확인된 데이터 -->', data)
            print('스택 상태 -->', stack)

        elif select == 'X' or select == 'x':
            print('프로그램 종료')
            break
        else:
            print('입력이 잘못됨')