# 주석 
'''
작성자 : 나
작성일자 : 220412
'''
# 출력 함수 예제
print('Hello, World')


==================실행 결과====================
Hello, World


# print 함수 <표준 출력>

print('안녕') #문자는 앞뒤로 작은 따옴표 또는 큰 따옴표를 넣는다.
              #파이썬은 작은 따옴표랑 큰 따옴표 구분이 없다.
print()       #파이썬의 print함수는 기본적으로 엔터를 포함한다.
print(3*4)
print(1)
print(2)      #숫자는 따옴표를 쓰지 않는다.

print(1, 2, 3) # 쉼표는 실행 시 스페이스(공백)기능을 한다.
print('안녕', '메롱')
print()

                        # sep
print(1, 2, 3, sep=',') # 출력 시 사이사이에 ''에 있는 문자가 나오도록 한다.
print(4, 5, 6, sep=':') # 출력 시 사이사이에 :이 나오도록 한다.
print()



                        # 끝에 ''에 있는 문자를 추가한다.
print(7, end='')        # 엔터 기능을 없앤다.
print(8, end='     ')   # 엔터기능 대신에 공백글자(스페이스)를 넣는다.
print(9)
print(10)

==================실행 결과====================
안녕

12
1
2
1 2 3
안녕 메롱

1,2,3
4:5:6

78     9
10




# 변수
 상자 또는 그릇에 내용물을 담앗다 라는 의미
 <형식>
 변수 이름 = 값
 ( = : 대입 연산자(assignment operator))

 예약어 (키워드) : 특별한 의미가 부여된 단어
                   파이썬에서 미리 특정 의미로 사용하기로 약속해 놓은 것
                   프로그래밍에서 이름을 정할 때 똑같이 사용 못 함
                   대소문자 구문
                   ex) for, if, and,,,,
                   


#예약어 (키워드) 확인하는 방법

import keyword

print(keyword.kwlist)

==================실행 결과====================

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# 32p

name = 'Alice'
age = 25
address = '''우편번호 12345
서울시 영등포구 여의도동
서울빌딩 501호''' # '''~''' 문자열을 나타냄.

boyfriend = None  # None : 없다.
height = 168.5

print(name)
print(age)
print(address)
print(boyfriend)
print(height)

==================실행 결과====================

Alice
25
우편번호 12345
서울시 영등포구 여의도동
서울빌딩 501호
None
168.5


# 여러개의 변수
a, b, c =1, 2, 3 # 변수 a, b, c 값에 각각 1 2 3 을 대입

print(a,b,c)


a=b=c=4 # 여러개의 변수에 한번에 같은값을 대입하는것도 가능

print(a,b,c)

#변수의 교환
a = 1
b = 2

print('변수 a :' ,a)
print('변수 b :' ,b)

a , b = b , a           # 변수 교환

print('변수 a :' ,a)
print('변수 b :' ,b)
                        # 파이썬에서는 변수의 맞교환 가능
                        
                        
==================실행 결과====================

1 2 3
4 4 4
변수 a : 1
변수 b : 2
변수 a : 2
변수 b : 1



# 자료형
     프로그래밍 할 때 쓰이는 숫자, 문자열 등 자료형태로 사용하는 모든 것
     다른 언어의 경우 변수 설정 시 애초에 타입을 설정해야하는 경우가 많음
     파이썬의 경우는 값을 할당하면 그때 타입이 결정되기 때문에
     초보자가 배우기 쉽다.

     type함수로 자료형을 볼 수 있다.


# 정수 변환

print(int(1.9))
print(int(True))    # 참은 1
print(int(False))   # 거짓은 0
print(int('100'))
print()

# 진수 변환

n = 95

print(bin(n))       # n을 2진수로 변환

print(oct(n))       # n을 8진수로 변환

print(hex(n))       # n을 16진수로 변환
print()

# 실수로 변환

print(float(1))     # 정수 1을 실수로

print(float(True))

print(float(False))

print(float('3.14'))

print(float('100'))
print()

# 논리형

print(bool(0))
print(bool(1))
print(bool(2))  # 0을 제외한 모든 수는 참이된다.
print(bool('')) # 비어있는 값은 거짓
print(bool([]))
print()

# 문자열

print('Hello, Python')  # 작은 따옴표
print("Hello, Python")  # 큰 따옴표

print('''Life is too short,
you need python''')     # 여러줄 입력할때는 따옴표 3개를 시작과 함께 넣기

print("It's me.")       # 어퍼스트로피 넣을때 편함

print('"파이썬 아주 쉽네."라고 그가 말했다.')     # 인용문 넣을때

print(str(100))
print(str(True))
print(str(False))
print(str(3.14))

==================실행 결과====================

1
1
0
100

0b1011111
0o137
0x5f

1.0
1.0
0.0
3.14
100.0

False
True
True
False
False

Hello, Python
Hello, Python
Life is too short,
you need python
It's me.
"파이썬 아주 쉽네."라고 그가 말했다.
100
True
False
3.14


# 문자열 인덱싱 (Indexing)

    [0] : 문자열의 처음을 뜻함
    [-1] : 문자열의 마지막을 뜻함

print('안녕하세요'[0])
print('안녕하세요'[1])
print('안녕하세요'[2])
print('안녕하세요'[3])
print('안녕하세요'[4])
print()

print('안녕하세요'[-1])
print('안녕하세요'[-2])
print('안녕하세요'[-3])
print('안녕하세요'[-4])
print('안녕하세요'[-5])
print()



a = 'My python'

print(a[0])
print(a[1])
print(a[2])     # 공백도 글자다 (인덱싱에 포함)
print(a[3])
print(a[-1])

==================실행 결과====================

안
녕
하
세
요

요
세
하
녕
안

M
y
 
p
n


# 문자열 슬라이싱 (slicing)
    문자열의 구간을 표시
    예를 들어 a라는 변수가 있다면
    a[시작번호 : 끝번호 +1]

    [:] -> 처음부터 끝까지. 모두를 의미


print('안녕하세요'[1:3])
print('안녕하세요'[2:5])
print()

a = 'python'
print(a[0:2])
print(a[:])
print(a[-2:-1])

print(a[:3])    # 처음부터 (시작번호 생략 가능)
print(a[2:])    # 끝까지 (끝번호를 생략)
print()

b = 'hello'
print(b[1])     # 인덱싱
print(b[2:4])   # 슬라이싱
print(b)        # 인덱싱, 슬라이싱을 한다고해서 원본에 영향을 주지않는다.

==================실행 결과====================

녕하
하세요

py
python
o
pyt
thon

e
ll
hello    











