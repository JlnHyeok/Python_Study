# 클래스
'''
[문제]

TV를 클래스로 정의하자.

변수(속성) : 채널(channel), 볼륨(volume), 전원상태(on)
함수(메서드) : turnOn() --> TV를 켠다.
              turnOff() --> TV를 끈다.
              setChannel(channel) --> 채널을 변경한다.
              setVolume(volume) --> 볼륨을 변경한다.


[출력결과]

TV 전원 : True
TV 볼륨 : 10
TV 채널 : 2
TV 전원 : False


[정답] 다양하게 풀 수 있으니 정답은 참고만 하시오.

class TV:
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.on = False

    def turnOn(self):
        self.on = True
        print(f'TV 전원 : {self.on}')

    def turnOff(self):
        self.on = False
        print(f'TV 전원 : {self.on}')

    def setVolume(self, volume):
        self.volume = volume
        print(f'TV 볼륨 : {self.volume}')

    def setChannel(self, channel):
        self.channel = channel
        print(f'TV 채널 : {self.channel}')

tv = TV()
tv.turnOn()
tv.setVolume(10)
tv.setChannel(2)
tv.turnOff()
    
'''



'''
[문제]

Animal이라는 클래스를 만들자.

변수(속성) : name
함수(메서드) : speak()

Dog, Duck라는 클래스를 만들자.
이 클래스는 Animal 클래스를 상속받는다.


[출력결과]

동물들의 울음소리에 대해 알아봅시다!
강아지는 멍멍
오리는 꽥꽥


[정답] 다양하게 풀 수 있으니 정답은 참고만 하시오.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name}들의 울음소리에 대해 알아봅시다!')

class Dog(Animal):
    def speak(self):
        print(f'{self.name}는 멍멍')

class Duck(Animal):
    def speak(self):
        print(f'{self.name}는 꽥꽥')

a = Animal('동물')
b = Dog('강아지')
c = Duck('오리')

a.speak()
b.speak()
c.speak()

'''
