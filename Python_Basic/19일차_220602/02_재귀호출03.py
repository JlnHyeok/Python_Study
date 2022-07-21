### 10부터 1까지의 합계를 재귀 호출로 구현 ###

def addNumber(num):
    if num <= 1:  # num이 1 이하면 1을 반환
        return 1
    return num + addNumber(num-1) # 그렇지 않으면 num-1을 재귀호출하고
                                  # num과 더한 값을 반환

print(addNumber(10))