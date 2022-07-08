### 별 모양 출력을 재귀 호출로 구현 ###

def printStar(n):
    if n > 0:
        printStar(n-1)  # 재귀 호출
        print('★' * n)  # 재귀 호출 다음에 나오는 문장은 역순으로 실행된다.

printStar(5)