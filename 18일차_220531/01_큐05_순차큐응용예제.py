### 순차 큐 응용 : 유명 맛집의 대기줄 구현하기

## 전역 변수 선언 부분

SIZE = 7
queue = [None for _ in range(SIZE)]
front = rear = -1

## 큐가 꽉 찼는지 확인하는 함수

def isQueueFull():
    global queue, front, rear
    if rear != SIZE-1:
        return False
    elif rear == SIZE-1 and front == -1:
        return True
    else:       # 앞쪽으로 당겨주는 구문
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

## 큐가 비었는지 확인하는 함수

def isQueueEmpty():
    if front == rear:
        return True
    else:
        return False

## 큐에 데이터를 삽입하는 함수

def enQueue(data):
    global queue, rear
    if isQueueFull():
        print('큐가 꽉 찼습니다')
        return
    rear += 1
    queue[rear] = data

## 큐의 데이터를 추출하는 함수

def deQueue():
    global queue, front, rear
    if isQueueEmpty():
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    # 두번째 손님부터 마지막 손님까지 한칸씩 이동
    for i in range(front+1, rear+1):
        queue[i-1] = queue[i]
        queue[i] = None
    front = -1  # 손님은 다시 첫번째 칸부터 대기하므로 -1로 초기화
    rear -= 1   # 마지막 손님 자리인 rear은 한칸 앞으로 당겨준다.
    return data

## 메인 코드 부분

if __name__ == '__main__':
    enQueue('정국')   # 손님을 대기줄에 세운다.
    enQueue('뷔')
    enQueue('지민')
    enQueue('진')
    enQueue('슈가')
    enQueue('RM')
    enQueue('제이홉')
    print('대기줄 상태 :',queue)
    for _ in range(rear+1):
        print(deQueue(),'님 식당에 들어감')    # 현재 대기줄의 손님을 식당에 입장시킨다.
        print('대기줄 상태 :',queue)
    print('식당 영업 종료')

