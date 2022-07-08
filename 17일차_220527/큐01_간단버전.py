### 크기가 5칸인 큐의 생성과 데이터 3개 입력

queue = [None, None, None, None, None]
front = rear = -1   # 초기상태(큐가 비어있는 상태)

rear += 1   # rear을 1 증가
queue[rear] = '화사'  # 데이터 삽입(큐의 0번째)
rear += 1
queue[rear] = '솔라'  # 데이터 삽입(큐의 1번째)
rear += 1
queue[rear] = '문별'  # 데이터 삽입(큐의 2번째)

print('----- 큐 상태 -----')
print('[출구] <--', end = ' ')
for i in range(len(queue)):
    print(queue[i], end = ' ')
print('<-- [입구]')
print('-------------------------------------------------')

### 큐에서 데이터를 3개 추출

front += 1  # front를 1 증가
data = queue[front] # 현재 front 위치의 데이터를 추출
queue[front] = None # front 위치에 None을 대입하여 데이터를 삭제

print('----- 큐 상태 -----')
print('[출구] <--', end = ' ')
for i in range(len(queue)):
    print(queue[i], end = ' ')
print('<-- [입구]')
print('-------------------------------------------------')

front += 1  # front를 1 증가
data = queue[front] # 현재 front 위치의 데이터를 추출
queue[front] = None # front 위치에 None을 대입하여 데이터를 삭제

print('----- 큐 상태 -----')
print('[출구] <--', end = ' ')
for i in range(len(queue)):
    print(queue[i], end = ' ')
print('<-- [입구]')
print('-------------------------------------------------')

front += 1  # front를 1 증가
data = queue[front] # 현재 front 위치의 데이터를 추출
queue[front] = None # front 위치에 None을 대입하여 데이터를 삭제

print('----- 큐 상태 -----')
print('[출구] <--', end = ' ')
for i in range(len(queue)):
    print(queue[i], end = ' ')
print('<-- [입구]')
print('-------------------------------------------------')