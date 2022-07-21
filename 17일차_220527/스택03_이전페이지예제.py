### 스택을 활용한 웹 브라우저의 이전페이지 버튼 기능 구현

import webbrowser
import time

## 전역 변수 선언 부분

SIZE = 100  # url은 최대 100개까지 방문하도록 설정
stack = [None for _ in range(SIZE)]     # 100개만큼
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
    urls = ['naver.com', 'daum.net', 'nate.com']     # 방문할 url

    for url in urls:
        push(url)    # 삽입 함수 호출
        webbrowser.open('http://' + url)    # 홈페이지를 연다.
        print(url, end='-->')
        time.sleep(1)   # 너무 동시에 접속되지 않도록 1초 멈춘 후 반복
    print('방문 종료')
    time.sleep(4)   # 모든 url 방문이 끝나면 4초간 멈춘다.

    while 1:
        url = pop()     # 스택에서 모든 url을 추출해서 방문(반대로)
        if url == None:     # 스택이 비었다면 종료
            break
        webbrowser.open('http://' + url)    # 홈페이지를 연다.
        print(url, end='-->')
        time.sleep(1)

    print('방문 종료')