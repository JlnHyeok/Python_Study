### 스택을 활용한 괄호 매칭 검사 구현

## 전역 변수 선언 부분

SIZE = 100
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

## 괄호 검사 함수 : 올바르면 True, 문제가 있으면 False 를 반환

def checkBraket(expr):
    for ch in expr:     # 수식 문자열에서 한 문자씩 추출해서 반복
        if ch in '([{<':    # 문자가 여는 괄호라면
            push(ch)        # 괄호를 스택에 삽입
        elif ch in ')]}>':      # 문자가 닫는 괄호라면
            out = pop()         # 스택에서 여는 괄호를 추출
            if ch == ')' and out =='(':     # 스택에서 추출한 것과 비교
                pass    # 같은 종류의 괄호라면 정상이므로 다시 반복문으로 올라간다.
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False    # 괄호 종류가 다르면 오류이므로 False 반환하고 함수 종료
        else:
            pass    # 괄호가 아닌 모든 문자는 별도 처리없이 그냥 넘어간다.
    if isStackEmpty():  # 모든 문자의 처리가 끝나면
        return True     # 스택이 비어 있어야 정상
    else:
        return False

## 메인 코드 부분

if __name__ == '__main__':
    # 검사할 문자열 exprAry
    exprAry = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B+C}/[C*D]>)']
    for expr in exprAry:    # 문자열 하나씩 처리
        top = -1    # 스택을 비운다.
        print(f'{expr} ==> {checkBraket(expr)}')    # 괄호 검사 함수 호출
        