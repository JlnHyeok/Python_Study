### 원형 큐 동작을 위한 통합 코드

## 전역 변수 선언 부분

SIZE = int(input('큐 크기를 입력해주세요 : '))
queue = [None for _ in range(SIZE)]
front = rear = 0    # 원형 큐 특징

## 원형 큐가 꽉 찬 경우

def isQueueFull():
    if (rear+1)%SIZE == front:  # rear다음이 front라면
        return True     # 원형 큐가 꽉 찾 상태
    else:
        return False

## 원형 큐가 빈 경우 함수

def isQueueEmpty():
    if front == rear:   # front와 rear이 같으면
        return True     # 원형 큐는 빈 상태
    else:
        return False

## 원형 큐 데이터 삽입 함수

def enQueue(data):
    global queue, rear
    if isQueueFull():
        print('큐가 꽉 찼습니다')
        return
    rear = (rear+1)%SIZE    # 큐 크기로 나눈 나머지로 구한다.
    queue[rear] = data      # 데이터 삽입

## 원형 큐 데이터 추출 함수

def deQueue():
    global queue, front
    if isQueueEmpty():
        return None
    front = (front +1)%SIZE
    data = queue[front]     # 데이터 추출
    queue[front] = None     # 데이터 삭제
    return data             # 데이터 반환

## 원형 큐 데이터를 확인하는 함수

def peek():
    if isQueueEmpty():
        return None
    return queue[(front+1)%SIZE]

## 메인 코드 부분

if __name__ == '__main__':
    while 1:
        select  = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 : ')
        if select == 'I' or select =='i':
            data = input('입력할 데이터: ')
            enQueue(data)   # 삽입 함수 호출
            print('큐 상태 : ', queue)
        elif select =='E' or select =='e':
            data = deQueue()    # 추출 함수 호출
            print('추출한 데이터 : ',data)
            print('큐 상태 : ', queue)
        elif select =='V' or select =='v':
            data = peek()   # 확인 함수 호출
            print('확인 된 데이터 : ',data)
            print('큐 상태 : ', queue)
        elif select =='X' or select =='x':
            print('프로그램 종료')
            break
        else:
            print("입력이 잘못됨")

