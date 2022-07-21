# ex) for문을 이용해서 파일에 문자열 쓰기

file = open('hello.txt','w')    # 파일 열기(쓰기 모드로)

# 'c:/a/hello.txt' --> c드라이브 안 a라는 폴더에 hello.txt파일을 생성한다.(절대경로)

# 상대경로 : 현재 폴더를 기준으로
# 절대경로 : 'C:/폴더명/폴더명.../파일명'

for i in range(1,11):
    data = f'{i}번째 줄입니다.\n'     # \n : 엔터
    file.write(data)    # write 함수는 엔터 기능이 없다.

file.close()    # 파일 닫기

======================실행 결과======================


# ex) for문을 이용해서 파일에 새로운 내용을 추가하기

f = open('hello.txt','a')   # 파일 열기(추가 모드로)

for i in range(11,21):
    data = f'{i}번째 줄입니다!!\n'
    f.write(data)

f.close()   # 파일 닫기

======================실행 결과======================
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
11번째 줄입니다!!
12번째 줄입니다!!
13번째 줄입니다!!
14번째 줄입니다!!
15번째 줄입니다!!
16번째 줄입니다!!
17번째 줄입니다!!
18번째 줄입니다!!
19번째 줄입니다!!
20번째 줄입니다!!


## 파일에서 문자열 읽기

    <형식>
    파일객체명 = open('파일 이름','r')
    변수명 = 파일객체명.read()
    파일객체명.close()

    print(변수명)  # 화면으로 보고 싶을 때 사용

# ex)

f = open('hello.txt','r')   # 파일 열기(읽기 모드로)

a = f.read()    # 읽은 내용을 a변수에 담았다.
f.close()   # 파일 닫기

print(a)

======================실행 결과======================
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
11번째 줄입니다!!
12번째 줄입니다!!
13번째 줄입니다!!
14번째 줄입니다!!
15번째 줄입니다!!
16번째 줄입니다!!
17번째 줄입니다!!
18번째 줄입니다!!
19번째 줄입니다!!
20번째 줄입니다!!


# 파일에서 여러 줄을 리스트로 각각 읽기

    <형식>
    파일객체명 = open('파일 이름','r')
    리스트명 = 파일객체명.readlines()
    파일객체명.close()

    print(리스트명)     # 화면에서 보고자 할 때


# ex)

f = open('hello.txt','r')   # 파일 읽기(읽기 모드로)
lines = f.readlines()   # 파일에서 읽은 내용을 리스트로 저장
f.close()   # 파일 닫기

print(lines)    # 리스트 형식인지 확인하려고 넣은 코드

for i in lines:     # 여러 줄을 한 줄씩 차례로 출력
    print(i,end='')     # print함수에 있는 엔터 기능을 없앤다. \n을 사용했어서 두칸씩 띄어진다

======================실행 결과======================
['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', '4번째 줄입니다.\n', '5번째 줄입니다.\n', '6번째 줄입니다.\n', '7번째 줄입니다.\n', '8번째 줄입니다.\n', '9번째 줄입니다.\n', '10번째 줄입니다.\n', '11번째 줄입니다!!\n', '12번째 줄입니다!!\n', '13번째 줄입니다!!\n', '14번째 줄입니다!!\n', '15번째 줄입니다!!\n', '16번째 줄입니다!!\n', '17번째 줄입니다!!\n', '18번째 줄입니다!!\n', '19번째 줄입니다!!\n', '20번째 줄입니다!!\n']
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
11번째 줄입니다!!
12번째 줄입니다!!
13번째 줄입니다!!
14번째 줄입니다!!
15번째 줄입니다!!
16번째 줄입니다!!
17번째 줄입니다!!
18번째 줄입니다!!
19번째 줄입니다!!
20번째 줄입니다!!


# with문과 함께 파일 입출력하기

    파일을 열면 항상 close 해주어야하는 불편함을 덜어주는 기능

    <형식>
    with open('파일 이름','파일 열기 모드') as 파일객체명:
        수행할 코드


# ex)

lista = ['Hello~\n','world\n','merong~\n','python!!\n']

with open('file.txt','w') as f:     # 쓰기 모드
    f.writelines(lista)     # 리스트를 파일에 쓸 때
    f.write('ㅋㅋㅋㅋ\n')
    f.write('파이썬 재밌어!\n')

with open('file.txt','r') as f:     # 읽기 모드
    b = f.read()    # 파일의 내용을 모두 읽어서 b변수에 담았다.

print(b)

======================실행 결과======================
Hello~
world
merong~
python!!
ㅋㅋㅋㅋ
파이썬 재밌어!


# 264p)

import time     # 시간/날짜를 처리하기 위한 모듈을 불러온다.
# strftime : 날짜,시간을 문자열 형식으로 , type이 str 형식이다.
# // strptime: 날짜 시간형식의 문자열을 datetime형식으로 , type이 datetime.datetime 형식이다
file = open(time.strftime('%Y-%m-%d') + '.txt', 'at')   # 날짜에 형식 지정 -> 파일명 a는 append, t는 txt형식. 생략가능
while 1:
    schedule = input('오늘의 스케쥴을 입력하세요 >>> ')
    if not schedule :   # 스케쥴이 없다면(아무것도 입력 안했다면)
        break
    file.write(schedule + '\n')     # 스케쥴 뒤에 엔터 삽입

file.close()    # 파일을 닫아준다.

======================실행 결과======================
오늘의 스케쥴을 입력하세요 >>> 공부
오늘의 스케쥴을 입력하세요 >>> 카페
오늘의 스케쥴을 입력하세요 >>> 독서
오늘의 스케쥴을 입력하세요 >>> 낮잠
오늘의 스케쥴을 입력하세요 >>> 


# 237p)

file = open('엄마돼지아기돼지.txt','rt')    # 파일 열기(읽기 모드로)

line_list = file.readlines()    # 전체 라인을 저장한 리스트, 리스트형태로 읽어준다.

count = 0   # 꿀의 개수

for line in line_list:  # 전체 라인 중 하나의 라인을 문자열 line 변수에 저장
    for ch in line:     # line에 담긴 모든 문자들을 하나씩 ch변수에 저장해서 비교
        if ch == '꿀':
            count += 1  # 꿀이 나오면 개수 증가

file.close()      # 파일 닫기

print('꿀은 전체 {}번 나타납니다.'.format(count))

======================실행 결과======================
꿀은 전체 54번 나타납니다.


# 객체 지향 프로그래밍 (Object-Oriented Programming, OOP)

     복잡한 문제를 작게 나누어 객체(object)를 만들고
     객체를 조합해서 문제를 해결하는 방식
     복잡한 문제를 처리하는데 유용하며, 기능을 개선하고 발전시킬 때도
     해당 클래스만 수정하면 되므로 유지 보수에 효율적

     클래스(class) : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계도
                    과자틀, 붕어빵틀에 비유
                    
     객체(object) : 붕어빵 틀에서 만들어 낸 붕어빵에 비유
                   각각의 객체마다 고유의 특성을 가진다.
                   파이썬에는 문자, 숫자, 리스트, 딕셔너리, 함수 등 모두 객체다.
                   
     인스턴스(instance) : 특정 객체가 어떤 클래스의 객체인지 관계 위주로 설명할 때 사용
                         클래스와 연관지어서 객체를 말할 때 인스턴스라고 한다.
                         
     메서드(method) : 클래스 안에서 구현된 함수

     <형식>
     class 클래스이름: # 파이썬에서는 클래스이름을 주로 대문자로 시작
         def 메서드이름(self, 매개변수):  # self란 메서드를 호출한 객체가 자동으로 전달되는 매개변수
             self.속성 = 값

     인스턴스이름 = 클래스이름()   # 인스턴스(객체) 생성
     인스턴스이름.메서드이름()     # 메서드 호출(함수 호출)


## 인스턴스 변수와 인스턴스 메서드

class Person:   # 클래스 정의
    def who_am_i(self, name, age, tel, address): # self가 있으면 인스턴스 메서드 정의
        self.name = name    # self가 붙으면 인스턴스 변수
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()  # boy라는 객체(인스턴스) 생성
boy.who_am_i('john', 15, '123-1234', 'toronto') # 메서드(함수) 호출
print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address) # self는 boy를 가리킨다.

boy2 = Person() # boy2 객체(인스턴스) 생성
boy2.who_am_i('ryan',20,'111-1111','Daegu') # 메서드(함수) 호출
print(boy2.name)
print(boy2.age)
print(boy2.tel)
print(boy2.address)

======================실행 결과======================
john
15
123-1234
toronto
ryan
20
111-1111
Daegu


# 267p)

class Computer:     # 클래스 정의
    def set_spec(self, cpu, ram, vga, ssd): # 인스턴스 메서드 정의
        self.cpu = cpu  # 인스턴스 변수(속성)
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):   # 인스턴스 메서드 정의
       print('CPU = {}'.format(self.cpu))
       print('RAM = {}'.format(self.ram))
       print('VGA = {}'.format(self.vga))
       print('SSD = {}'.format(self.ssd))
       print()

desktop = Computer()    # 객체(인스턴스) 생성
desktop.set_spec('i7','16GB','GTX1060','512GB')     # 메서드 호출
desktop.hardware_info()     # 메서드 호출

notebook = Computer()   # 객체(인스턴스) 생성
notebook.set_spec('i5','8GB','MX300','256GB')   # 메서드 호출
notebook.hardware_info()

======================실행 결과======================
CPU = i7
RAM = 16GB
VGA = GTX1060
SSD = 512GB

CPU = i5
RAM = 8GB
VGA = MX300
SSD = 256GB


# 269p)

class Calculator:   # 클래스 정의
    def input_expr(self):   # 인스턴스 메서드 정의
        expr = input('수식을 입력하세요 >>> ')
        self.expr = expr

    def calculate(self):    # 인스턴스 메서드 정의
        return eval(self.expr)  # eval() : 문자열로 된 수식을 계산해주는 함수

calc = Calculator() # 객체(인스턴스) 생성
calc.input_expr()   # 메서드 호출
print('수식 결과는 {} 입니다.'.format(calc.calculate()))

======================실행 결과======================
수식을 입력하세요 >>> (1+5+2)/2
수식 결과는 4.0 입니다.


# 생성자 (constructor)

    객체에 초기값을 설정해야 할 필요가 있을 때 사용
    객체가 생성될 때 자동으로 호출되는 메서드
    __init__ 를 사용
    
    스페셜메서드(매직메서드) : 파이썬에서 자동으로 호출해주는 메서드
                            앞뒤로 __가 붙은 메서드

    <형식>
    class 클래스이름:
        def __int__(self): # 생성자
            self.속성 = 값


# ex)

class Candy:    # 클래스 정의
    def set_info(self, shape, color):   # 인스턴스 메서드
        self.shape = shape
        self.color = color

satang = Candy()    # 객체(인스턴스) 생성
satang.set_info('circle','brown')   # 인스턴스 메서드 호출
print(satang.shape)
print(satang.color)
print()

print('----------------생성자----------------')

class Candy2:   # 클래스 정의
    def __init__(self, shape, color): # 생성자
        self.shape = shape
        self.color = color


satang2 = Candy2('triangle','red')  # 객체 생성과 동시에 생성자 호출
print(satang2.shape)
print(satang2.color)
print()

satang3 = Candy2('circle', 'pink')  # 객체 생성과 동시에 생성자 호출
print(satang3.shape)
print(satang3.color)

======================실행 결과======================
circle
brown

----------------생성자----------------
triangle
red

circle
pink

# 276p)

class USB:  # 클래스를 정의
    def __init__(self, capacity): # 생성자
        self.capacity = capacity

    def info(self): # 인스턴스 메서드 정의
        print('{}GB USB'.format(self.capacity))

usb = USB(64) # 객체(인스턴스) 생성
usb.info()    # 인스턴스 메서드 호출

usb2 = USB(128) # 객체(인스턴스) 생성
usb2.info()     # 인스턴스 메서드 호출

======================실행 결과======================
64GB USB
128GB USB








