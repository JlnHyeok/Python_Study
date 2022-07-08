### 스택을 이용한 헨젤과 그레텔의 집으로 돌아가기

import random

## 전역 변수 선언 부분

SIZE = 10
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
        #print('스택이 비었습니다.')
        return None
    data = stack[top]   # 데이터를 추출하고
    stack[top] = None   # 그 자리에 None을 대입하고 삭제
    top -= 1
    return data         # 추출한 데이터를 반환

## 스택에서 top 위치의 데이터를 확인하는 함수

def peek():
    if isStackEmpty():
        #print('스택이 비었습니다.')
        return None
    return stack[top] # 현재 top위치의 데이터를 반환

## 메인 코드 부분

if __name__ == '__main__':
    stoneAry = ['빨강', '파랑', '초록', '노랑', '보라', '주황'] # 임의의 돌 준비
    random.shuffle(stoneAry)    # 순서를 임의로 섞는다.
    print('과자집에 가는 길 :', end = ' ')
    for stone in stoneAry:
        push(stone) # 과자집에 가는 길에 떨어뜨린 돌의 색상을 스택에 삽입
        print(stone, '-->', end = ' ')      # 돌의 색상을 출력
    print('과자집')

    print('우리집에 오는길 :',end = ' ')
    while 1:
        stone = pop()   # 집으로 돌아가는 길에 스택에서 추출
        if stone == None:   # 돌이 없으면 집에 도착한 것이므로 종료
            break
        print(stone, '==>', end = ' ')  # 떨어뜨린 반대 순서로 출력
    print('우리집')
    

