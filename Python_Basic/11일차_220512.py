# 277p)

class Service: # 클래스 정의
    def __init__(self, service): # 생성자
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))

    def __del__(self): # 소멸자
        print('{} Service가 종료되었습니다.'.format(self.service))


s = Service('길 안내') # 객체(인스턴스) 생성
del s   # 객체(인스턴스) 삭제

======================실행 결과======================
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.

# 클래스 변수

    클래스 안에서 공간이 할당된 변수
    여러 인스턴스가 클래스 변수 공간을 함께 사용


# ex)

class Car:  # 클래스 정의
    count = 0   # 클래스 변수
    def __init__(self, name, speed):    # 생성자
        self.name = name    # 인스턴스 변수(속성)
        self.speed = speed
        Car.count += 1      # 클래수 변수에 1씩 증가

my_car = Car('붕붕카', 0)  # 객체(인스턴스) 생성
print(f'{my_car.name}의 현재 속도 : {my_car.speed}km, 생산된 자동차 수 : {Car.count}대')

bro_car = Car('빵빵카', 30)    # 객체(인스턴스) 생성
print(f'{bro_car.name}의 현재 속도 : {bro_car.speed}km, 생산된 자동차 수 : {Car.count}대')

sis_car = Car('띠띠카', 60)    # 객체(인스턴스) 생성
print(f'{sis_car.name}의 현재 속도 : {sis_car.speed}km, 생산된 자동차 수 : {Car.count}대')

======================실행 결과======================
붕붕카의 현재 속도 : 0km, 생산된 자동차 수 : 1대
빵빵카의 현재 속도 : 30km, 생산된 자동차 수 : 2대
띠띠카의 현재 속도 : 60km, 생산된 자동차 수 : 3대


## 클래스 메서드

    클래스 변수를 사용하는 메서드
    인스턴스 없어도 호출이 가능
    매개변수 self 대신, cls 사용
    @classmethod 데코레이터로 표시
    
    
# ex)
class Korean: # 클래스를 정의
    country = '한국' # 클래스 변수

    @classmethod
    def trip(cls, country): # 클래스 메서드 정의
        if cls.country == country:
            print('국내여행입니다.')
        else:
            print('해외여행입니다.')


Korean.trip('한국') # 객체 없이 호출
Korean.trip('미국')

======================실행 결과======================
국내여행입니다.
해외여행입니다.

# 282p)

class Bag: # 클래스 정의
    count = 0 # 가방 개수 (클래스 변수)

    def __init__(self): # 생성자
        Bag.count += 1  # 생성자 호출될 때 마다 1씩 증가

    @classmethod
    def sell(cls):      # 클래스 메서드 정의
        cls.count -= 1  # 호출될 때 마다 1씩 감소

    @classmethod
    def remain_bag(cls):    # 클래스 메서드 정의
        return cls.count

print('현재 가방 : {}개'.format(Bag.remain_bag()))
bag1 = Bag()    # 인스턴스(객체) 생성
bag2 = Bag()
bag3 = Bag()
print('현재 가방 : {}개'.format(Bag.remain_bag()))

bag1.sell()
bag2.sell()
print('현재 가방 : {}개'.format(Bag.remain_bag()))

======================실행 결과======================
현재 가방 : 0개
현재 가방 : 3개
현재 가방 : 1개

## 클래스 상속

    어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만든것

    <형식>
    class 클래스이름(상속할 클래스이름):
        수행할 코드

    class 서브클래스(슈퍼클래스):
        수행할 코드

    class 자식클래스(부모클래스):
        수행할 코드

    
# ex)

class Person:   # 슈퍼클래스(부모클래스)
    def __init__(self, name):   # 생성자
        self.name = name

    def eat(self, food):    # 인스턴스 메서드
        print(f'{self.name}가 {food}를 먹습니다.')

class Student(Person):  # 서브클래스(자식클래스)
    def __init__(self, name, school):    # 자식의 생성자
       super().__init__(name)   # 슈퍼(부모)클래스의 생성자 호출
       self.school = school

    def study(self):    # 인스턴스 메서드
        print(f'{self.name}는 {self.school}에서 공부를 합니다.')                                                                                                                               


potter = Student('해리포터','호그와트')     # 객체(인스턴스) 생성
potter.eat('감자')    # 상속받은 메서드를 호출
potter.study()      # 인스턴스 메서드 호출

======================실행 결과======================
해리포터가 감자를 먹습니다.
해리포터는 호그와트에서 공부를 합니다.


# 286p)

class Coffee:   # 슈퍼클래스(부모클래스)
    def __init__(self, bean):   # 생성자
        self.bean = bean

    def coffee_info(self):  # 인스턴스 메서드 정의
        print('원두 : {}'.format(self.bean))

class Espresso(Coffee):     # 서브클래스(자식클래스)
    def __init__(self, bean, water): # 생성자
        super().__init__(bean)  # 부모의 생성자 호출
        self.water = water

    def espresso_info(self):    # 자식의 인스턴스 메서드
        super().coffee_info()   # 부모 클래스의 메서드 호출
        print('물 : {}ml'.format(self.water))

coffee = Espresso('콜롬비아',30)    # 객체(인스턴스) 생성
coffee.espresso_info()  # 인스턴스 메서드 호출

coffee2 = Espresso('예가체프',50)   # 객체(인스턴스) 생성
coffee2.espresso_info()

coffee3 = Espresso('맥심모카골드',60)     # 객체(인스턴스) 생성
coffee3.espresso_info()

======================실행 결과======================
원두 : 콜롬비아
물 : 30ml
원두 : 예가체프
물 : 50ml
원두 : 맥심모카골드
물 : 60ml

## 메서드 오버라이딩(재정의)

    부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것
    부모 클래스의 메서드 대신 오버라이딩(덮어쓰기)한 메서드가 호출된다.
    프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 활용
    

# 파일 입출력의 활용

## 파일 복사

buffer_size = 1024  # 한번에 읽어들이는 데이터의 크기(1kb == 1024byte)
with open('code.mp4','rb') as source:   # 동영상을 바이너리 모드로 읽는다.(rb)
    with open('code2.mp4','wb') as copy:    # 복사할 동영상을 바이너리 모드로 쓴다.
        while 1:
            buffer = source.read(buffer_size)   # 1024만큼 읽어서 buffer에 담는다.
            if not buffer:  # 버퍼의 내용이 없다면 중지
                break
            copy.write(buffer)  # 버퍼의 내용을 복사할 파일에 기록

print('code2.mp4 파일이 복사되었습니다.')

======================실행 결과======================
code2.mp4 파일이 복사되었습니다.


## CSV 파일 입출력

# CSV 파일 읽기

student_list = []   # 최종 결과를 담을 빈 리스트를 만든다.

with open('학생명단.csv','rt') as file:
    file.readline()     # 제목 라인이 날려진다.(0번째 인자를 읽음으로써 1번째인자부터 담는다.)
    while 1:
        line = file.readline()  # 한 줄씩 읽어 line 리스트에 담는다.
        if not line:    # 더 이상 라인이 없을 때까지 반복
            break
        student = line.split(',')   # ,로 구분된 것들을 분리하여 student리스트에 담는다.

        student_list.append(student)    # 결과 리스트에 분리한 student리스트 내용을 담는다.

print(student_list)     # 결과 출력

======================실행 결과======================
[['10101', '김승별', '서울시 영등포구', '010-1111-1111\n'], ['10102', '박나라', '서울시 여의도구', '010-2222-2222\n'], ['10103', '최태욱', '서울시 강남구', '010-3333-3333\n'], ['10104', '민기홍', '인천시 계양구', '010-4444-4444\n'], ['10105', '이명숙', '경기도 과천시', '010-5555-5555\n']]


# 247p)

member_list = []
with open('회원명단.csv','rt') as file:
    file.readline()     # 제목 라인 삭제
    while 1:
        line = file.readline()  # 한줄씩 읽어서 담겠다
        if not line:
            break
        member = line.split(',')    
        member[0] = member[0].strip('"')    # 0번 인덱스 값의 양쪽 "를 제거한다.
        member_list.append(member)

print(member_list)

======================실행 결과======================
[['강나라', '필라테스', '25일\n'], ['나유라', '수영', '25일\n'], ['이상기', '헬스', '15일\n']]

