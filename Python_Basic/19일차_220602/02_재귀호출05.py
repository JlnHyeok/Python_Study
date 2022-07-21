### 카운트다운을 재귀 호출로 구현 ###

def countDown(n): # 매개변수 n은 카운트다운할 숫자
    if n == 0:   # 숫자 0이면 발사를 출력하고 종료
        print('발사!!')
    else:
        print(n)
        countDown(n-1)  # 숫자-1을 재귀 호출

countDown(5)