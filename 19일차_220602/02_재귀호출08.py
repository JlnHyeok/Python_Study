### 피보나치 수를 재귀 호출로 구현 ###

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print('피보나치 수 --> 0 1', end=' ')  # 0과 1은 그대로 출력
for i in range(2, 20):  # 2번째 위치부터 19번째 위치까지 피보나치 수를 구한다.
    print(fibo(i), end=' ')





