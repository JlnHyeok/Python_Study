# 섹션 17 응용예제 1)

class Quiz:
    answer = ['경기도','강원도','충청남도','충청북도','전라남도','전라북도',
              '경상남도','경상북도','제주특별자치도'] # 클래스 변수
    @classmethod
    def challange(cls): # 클래스 메서드 정의
        if not cls.answer: # answer 리스트에 값이 없다는 뜻은 모두 맞췄다는 뜻.
            print('모든 도를 맞췄습니다. 성공입니다.')
            return # 함수 종료
        do = input('정답은? >>> ')
        if do not in cls.answer: # 대답이 answer 리스트에 없는 값이라면
            raise Exception('틀렸습니다')
        for i, answer_do in enumerate(cls.answer):
            if do == answer_do: # 정답과 대답이 같다면
                print('정답입니다.')
                cls.answer.pop(i)   # i번째 값을 꺼내어서 삭제
                break
        cls.challange()

try:
    print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
    Quiz.challange()    # 클래스 메서드 호출
except Exception as e:
    print(e)    # 예외 메시지 출력

======================실행 결과======================
우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.
정답은? >>> 경기도
정답입니다.
정답은? >>> 강원도
정답입니다.
정답은? >>> 충청남도
정답입니다.
정답은? >>> 충청북도
정답입니다.
정답은? >>> 전라남도
정답입니다.
정답은? >>> 전라북도
정답입니다.
정답은? >>> 경상남도
정답입니다.
정답은? >>> 경상북도
정답입니다.
정답은? >>> 제주특별자치도
정답입니다.
모든 도를 맞췄습니다. 성공입니다.


# 섹션 17 응용예제 2)

import random

class UpDown:
    def __init__(self): # 생성자
        self.answer = random.randint(1,100) # 1에서 100까지의 무작위 수 지정
        self.count = 0  # 시도 횟수

    def challange(self): # 인스턴스 메서드
        self.count += 1  # 시도 횟수를 1 증가
        n = int(input('입력 (1~100) : ')) # 사용자로부터 숫자를 입력받음
        if n < 1 or  n > 100: # 1~100 외의 숫자면 예외 발생시킴
            raise Exception('1~100 사이만 입력하세요.')
        return n # 입력값을 반환

    def play(self): # 인스턴스 메서드
        while 1:
            try:
                n = self.challange() # 숫자를 입력받음/challange에 있는 n이 여기 n에 담긴다.
                                     # challange 메서드를 여기에서 실행.
            except Exception as e:  # 예외 메시지 출력
                print(e)
            else:   # 예외가 발생하지 않았다면 (정상적이라면)
                if self.answer < n:
                    print('Down!!')
                elif self.answer > n:
                    print('Up!!')
                else:
                    print('{}번 만에 정답입니다.'.format(self.count))
                    break

game = UpDown() # 객체 인스턴스 생성
game.play()     # 인스턴스 메서드 호출

======================실행 결과======================
입력 (1~100) : 55
Up!!
입력 (1~100) : 82
Up!!
입력 (1~100) : 91
Down!!
입력 (1~100) : 88
Up!!
입력 (1~100) : 90
Down!!
입력 (1~100) : 89
6번 만에 정답입니다.


# 섹션 17 응용예제 3)

class BankError(Exception):     # 예외 클래스
    def __init__(self, message):
        super().__init__(message)   # Exception class의 생성자 호출

class BankAccount:
    # 생성자
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no    # 계좌번호
        self.balance = balance  # 통장 잔액

    # 입금 기능
    def deposit(self, money):
        if money <= 0:  # 0원 이하를 입금하려고 하면 예외 발생
            raise BankError('{}원 입금 불가'.format(money))
        self.balance += money   # 입금

    # 출금 기능
    def withdraw(self, money):
        if money <= 0:  # 0원 이하를 출금하려고 하면 예외 발생
            raise BankError('{}원 출금 불가'.format(money))
        if money > self.balance:  # 잔액보다 많이 출금하려고 하면 예외 발생
            raise BankError('잔액 부족')
        self.balance -= money   # 출금
        return money    # 출금한 금액을 반환

    # 이체 기능
    def transfer(self, your_acc, money): # 상대방 계좌, 이체할 금액
        your_acc.deposit(self.withdraw(money))

    # 조회 기능
    def inquiry(self):
        print('계좌번호 : {}'.format(self.acc_no))
        print('통잔잔액 : {}원'.format(self.balance))

# 정상 상황

me = BankAccount('012-34-56789',50000)
you = BankAccount('987-65-43210',50000)
try:
    me.transfer(you, 5000)
except BankError as e:
    print(e)
finally:    # 무조건 출력
    me.inquiry()
    you.inquiry()

======================실행 결과======================
계좌번호 : 012-34-56789
통잔잔액 : 45000원
계좌번호 : 987-65-43210
통잔잔액 : 55000원





