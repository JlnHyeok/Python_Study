# 모듈과 import

## 모듈을 불러와서 사용하기

    <형식>
    import 모듈이름 as 별칭   # as 별칭은 안해도 괜찮음
    또는
    from 모듈이름 import 모듈함수
    --> 모듈 이름을 생략하고 함수만 쓰고 싶을 때
    from 모듈이름 import *
    --> 모듈 안에 있는 모든 함수를 쓸 때 모두의 의미를 가진 *를 사용


# ex) import 방식

import m    # m 이라는 모듈을 불러온다.

print(m.add(1, 2))  # m 모듈에 있는 add 함수를 호출
print(m.sub(2, 1))
print(m.mul(1, 2))
print(m.div(2, 1))
print(m.mod(5, 2))

======================실행 결과======================
3
1
2
2.0
1


# ex) from 방식 (1)

from m import add, sub  # m 모듈에 있는 add, sub 함수를 가져온다.

print(add(1, 2))    # from으로 가져올 때는 모듈명이 필요없다.
print(sub(2, 1))    # m 모듈에 있는 sub 함수를 호출한 결과가 출력

======================실행 결과======================
3
1


# ex) from 방식 (2)

from m import *     # m 모듈에 있는 모든 함수를 가져온다.

x = int(input('x를 입력하세요 : '))
y = int(input('y를 입력하세요 : '))

n1 = add(x, y)  # m 모듈 안에 있는 함수 add의 결과값을 n1에 담았다.
n2 = sub(x, y)
n3 = mul(x, y)
n4 = div(x, y)
n5 = mod(x, y)

print('x + y =',n1)
print('x - y =',n2)
print('x * y =',n3)
print('x / y =',n4)
print('x % y =',n5)

print('n1 + n2 =', add(n1, n2))     # 리턴한 결과값 n1, n2가 다시 매개변수로 들어간다.
print('n3 - n4 =', sub(n3, n4))     

======================실행 결과======================
x를 입력하세요 : 3
y를 입력하세요 : 5
x + y = 8
x - y = -2
x * y = 15
x / y = 0.6
x % y = 3
n1 + n2 = 6
n3 - n4 = 14.4

## 패키지 (폴더)를 만들어서 관리

    <형식>
    import 패키지명(폴더명).모듈이름 as 별칭
    또는
    from 패키지명(폴더명).모듈이름 import 모듈함수

# ex)

from pkg.m import add, sub  # pkg 폴더 안 m 모듈에 있는 add, sub 함수를 불러온다.

print(add(1, 2))
print(sub(2, 1))

## __name__

    원래 파일에서 실행하면 __name__에 '__main__'이 할당
    모듈로 참조하고있는 다른 파일에서 실행하면
    __name__에 해당 모듈명이 할당됨.


from m import *

print(mul(1, 2))
print(div(2, 1))

======================실행 결과======================
m   # m 모듈에 있는 print문이 m으로 출력됨.
2
2.0
    

# 209p)

from my_secure import *

print(secure_name('김철수'))
print(secure_no('951012-1234567'))
print(secure_phone('010-1234-5678'))

======================실행 결과======================
김**
951012-1******
010-****-5678


# 표준 모듈

## math 모듈

import math     # 수학에 관련된 함수를 가진 모듈을 불러온다.

print(math.pi)  # 원주율

print(math.ceil(1.1))   # 올림
print(math.floor(1.9))  # 내림

print(math.trunc(-1.6))     # 버림
print(math.floor(-1.6))     # -1.6보다 더 작은 정수로 내림

print(math.sqrt(25))    # 제곱근

print(math.pow(2, 3))   # 2의 3 제곱   2**3

======================실행 결과======================
3.141592653589793
2
1
-1
-2
5.0
8.0


# random 모듈

import random   # 난수 생성하는 모듈

print(random.randint(1, 10))    # 1~10 정수 중 아무 숫자

print(random.randrange(10))     # 0~9 중 아무 숫자
print(random.randrange(1, 10))  # 1~9 중 아무 숫자
print(random.randrange(1, 10, 2))   # 1,3,5,7,9 중 아무 숫자

print(random.random())  # 0이상 1 미만 중 아무 숫자

seasons = ['spring','summer','fall','winter']
print(random.choice(seasons))   # seasons 리스트 값 중 하나

print(random.sample(range(1,46),6))     # 중복 없이 6개의 숫자를 리스트 형태로 출력

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)     # 임의로 섞기
print(my_list)

======================실행 결과======================
6
8
3
9
0.41835414670076576
fall
[19, 10, 39, 40, 42, 15]
[2, 1, 5, 4, 3]


# ex) 램덤 모듈을 이용해서 무작위로 덧셈 문제를 만들어서 맞추기

import random

num1 = random.randint(1, 10)    # 1~10 사이의 수 중 임의의 정수를 num1에 저장
num2 = random.randint(1, 10)

ans = int(input(f'{num1} + {num2} = '))

if ans == num1 + num2:  # 내가 입력한 정답과 더한 값을 비교
    print('정답입니다')
else:
    print('오답입니다')

======================실행 결과======================
9 + 6 = 15
정답입니다


# 213p)

import random

dice = random.randint(1,6)

while 1:
    ans = int(input('주사위 눈을 맞춰보세요 : '))

    if ans == dice:
        print('정답입니다')
        break
    else:
        print('오답입니다, 다시 입력해주세요')

======================실행 결과======================
주사위 눈을 맞춰보세요 : 2
오답입니다, 다시 입력해주세요
주사위 눈을 맞춰보세요 : 1
오답입니다, 다시 입력해주세요
주사위 눈을 맞춰보세요 : 4
정답입니다

# ex) 모듈과 조건문을 이용한 계절 구하기

import datetime

now = datetime.datetime.now()   # 현재 날짜와 시간을 가져온다. (pc로 부터)
m = now.month   # 추출한 현재 날짜시간 변수에 있는 월만 따로 m변수에 저장

if 3 <= m <= 5:     # 만약 월이 3,4,5월이라면
    print('봄입니다')
elif 6<= m <= 8:
    print('여름입니다')
elif 9<= m <= 11:
    print('가을입니다')
else:   # 12, 1, 2
    print('겨울입니다')

======================실행 결과======================
봄입니다


# ex) 모듈을 이용한 속으로 10초 세어 맞히는 프로그램

import time

input('엔터를 누르고 10초를 셉니다')
start = time.time()     # 현재 시간을 저장

input('10초 후에 다시 엔터를 누릅니다')
end = time.time()

es = end - start    # 두 시간의 차이를 구한다.

print(f'실제시간 : {es}초')
print(f'차이 : {abs(es-10)}초')    # abs() --> 절대값

======================실행 결과======================
엔터를 누르고 10초를 셉니다
10초 후에 다시 엔터를 누릅니다
실제시간 : 11.825641870498657초
차이 : 1.8256418704986572초


# 218p)

from datetime import *

start = datetime.now()  # 계산하기 전 현재 시간
total = 0
for num in range(1, 10000001):
    total += num
    
end = datetime.now()    # 계산 완료 후 현재 시간
es = end - start        # 두 시간의 차이
es = es.total_seconds()     # 초 단위로 변환

print(f'총 합은 {total}입니다.')
print(f'계산하는데 걸린 시간은 {es}초 입니다.')

======================실행 결과======================
총 합은 50000005000000입니다.
계산하는데 걸린 시간은 0.687337초 입니다.


# 파일 입출력

## 파일 생성하고 문자열 쓰기

    <형식> (기본 방법)
    파일객체명 = open('파일 이름','w')
    파일객체명.write('문자열')
    파일객체명.write(str(숫자))   # write함수는 문자형식만 가능
    파일객체명.close()   # 파일을 닫아준다

    <형식> (리스트 사용)
    리스트명 = [값1, 값2,...]
    파일객체명 = open('파일 이름','w')
    파일객체명.writelines(리스트명)
    파일객체명.close()
    
# ex)

file = open('hello.txt','w')    # 파일 열기(쓰기 모드로)
file.write('Hello, world!')
file.close()    # 파일 닫기

======================실행 결과======================
Hello, world!


