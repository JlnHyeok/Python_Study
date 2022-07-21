### 팩토리얼을 재귀 호출로 구현 ###

# 팩토리얼(Factorial) : 특정 숫자부터 1까지 곱하는 것
# 5! = 5 * 4 * 3 * 2 * 1

def factorial(num):
    if num <= 1:  # num이 1 이하면 1을 반환
        print('1 반환')
        return 1
    print(f'{num} * {num-1}! 호출')
    retVal = factorial(num-1)  # num-1을 재귀 호출

    # 재귀 호출이 모두 끝나고 반환되면
    print(f'{num} * {num-1}!(={retVal}) 반환')
    return num * retVal # num * (num-1)!의 값을 반환한다.

print('5! =', factorial(5))



