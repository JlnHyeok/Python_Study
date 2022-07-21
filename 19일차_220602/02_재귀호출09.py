### 회문 여부 구별하기 ###

## 전역 변수 선언 부분 ##
strAry = ['reaver', 'kayak', 'Borrow or rob', '주유소의 소유주',
          '야 너 이번 주 주번이 너야', '살금 살금']

## 함수 선언 부분 ##
def palindrome(pStr):
    if len(pStr) <= 1:  # 문자열의 길이가 1 이하라면 회문으로 처리
        return True
    if pStr[0] != pStr[-1]: # 문자열의 맨 앞과 마지막 글자가 다르면 회문이 아닌 것으로 처리
        return False
    # 회문 여부가 결정되지 않았다면, 앞뒤 한 칸씩 잘라내고 다시 재귀함수 호출
    return palindrome(pStr[1:len(pStr)-1])

for testStr in strAry:
    print(testStr, end='-->')
    testStr = testStr.lower().replace(' ', '') # 소문자로 만든 후 사이의 공백을 제거
    if palindrome(testStr):
        print('O')
    else:
        print('X')








