### 크기가 5칸인 스택의 생성과 데이터 3개 입력

stack = [None, None, None, None, None]
top = -1

top += 1  # top를 0으로 만들고
stack[top] = '커피'   # 배열의 0번째 데이터 입력
top += 1
stack[top] = '녹차'   # 배열의 1번째 데이터 입력
top += 1
stack[top] = '꿀물'   # 배열의 2번째 데이터 입력

print('-------스택 상태-------')
for i in range(len(stack)-1,-1,-1):
    print(stack[i])     # 4,3,2,1,0번째 데이터가 차례로 출력
print('-------스택 상태-------')

### 스택에서 데이터 3개 추출

data = stack[top]   # top위치의 데이터 추출
stack[top] = None   # None 를 대입하려 데이터를 삭제한다
top -= 1
print('pop --->', data)
print('-------스택 상태-------')
for i in range(len(stack)-1,-1,-1):
    print(stack[i])     # 4,3,2,1,0번째 데이터가 차례로 출력
print('-------스택 상태-------')

data = stack[top]   # top위치의 데이터 추출
stack[top] = None   # None 를 대입하려 데이터를 삭제한다
top -= 1
print('pop --->', data)
print('-------스택 상태-------')
for i in range(len(stack)-1,-1,-1):
    print(stack[i])     # 4,3,2,1,0번째 데이터가 차례로 출력
print('-------스택 상태-------')

data = stack[top]   # top위치의 데이터 추출
stack[top] = None   # None 를 대입하려 데이터를 삭제한다
top -= 1
print('pop --->', data)
print('-------스택 상태-------')
for i in range(len(stack)-1,-1,-1):
    print(stack[i])     # 4,3,2,1,0번째 데이터가 차례로 출력
print('-------스택 상태-------')