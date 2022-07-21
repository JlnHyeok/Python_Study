### 큐 동작을 위한 기능 개선 버전

## 전역 변수 선언 부분

SIZE = int(input('큐 크기를 입력해주세요 :'))
queue = [None for _ in range(SIZE)]
rear = front = -1

## 큐가 꽉 찼는지 확인하는 함수

def isQueueFull():
    global queue, front, rear
    if rear != SIZE-1:  # rear 뒤에 빈칸이 있는 상태인지 확인
        return False    # 큐가 꽉 차지 않았다.
    elif rear == SIZE-1 and front == -1:    # 큐가 꽉 찬 상태인지 확인
        return True     # 큐가 꽉 찼다.
    else:   # rear이 큐크기-1과 같지만 앞부분에 빈칸이 있다.
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]   # 앞으로 한 칸씩 이동
            queue[i] = None         # 이동시킨 칸을 빈 칸으로 만든다.
        front -= 1      # front를 왼쪽으로 한 칸 이동시키고
        rear -= 1       # rear을 왼쪽으로 한 칸 이동시킨다.
        return False    # 이제 큐 마지막 칸이 비었으므로 False 반환

## 큐가 비었는지 확인하는 함수

def isQueueEmpty():
    if front == rear:   # front와 rear의 위치가 서로 같다면
        return True     # 큐가 비었다.
    else:
        return False

## 큐에 데이터를 삽입하는 함수

def enQueue(data):
    global queue, rear
    if isQueueFull():   # 큐가 꽉 찼는지 확인하고
        print('큐가 꽉 찼습니다')
        return  # 꽉 찼으면 함수 종료
    rear += 1   # rear을 1 증가시키고
    queue[rear] = data  # 데이터 입력

## 큐에서 데이터를 추출하는 함수

def deQueue():
    global queue, front
    if isQueueEmpty():  # 큐가 비었는지 확인
        print('큐가 비었습니다')
        return None
    front += 1  # front위치를 1 증가
    data = queue[front] # front위치의 데이터를 추출
    queue[front] = None # 현재 front자리에 None을 대입하여 삭제
    return data         # 추출한 데이터를 반환

## 큐에서 front +1 위치의 데이터(첫번째 데이터)를 확인하는 함수
def peek():
    if isQueueEmpty():
        print('큐가 비었습니다')
        return None
    return queue[front+1]   # 데이터 확인만 한다.

## 메인 코드 부분

if __name__ == '__main__':
    while 1:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 -->')
        if select == 'I' or select == 'i':
            data = input('입력할 데이터 -->')
            enQueue(data)   # 삽입 함수 호출
            print('큐 상태 -->', queue)
        elif select == 'E' or select == 'e':
            data = deQueue()    # 추출 함수 호출
            print('추출된 데이터 -->', data)
            print('큐 상태 -->', queue)
        elif select == 'V' or select == 'v':
            data = peek()   # 확인 함수 호출
            print('확인된 데이터 -->', data)
            print('큐 상태 ==>', queue)
        elif select == 'X' or select == 'x':
            print('프로그램 종료')
            break
        else:
            print('입력이 잘못됨')

