### 구구단 출력을 재귀 호출로 구현 ###

def gugu(dan, num):
    print(f'{dan} x {num} = {dan * num}')
    if num < 9:  # 곱할 숫자(num)가 9보다 작다면 함수를 재귀 호출
        gugu(dan, num+1)

for dan in range(2, 10):
    print(f'##{dan}단##')
    gugu(dan, 1)