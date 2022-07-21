# 시퀀스 내장 함수

# enumerate()   for 문에서만 사용 가능

    <형식>
    for 인덱스 번호, 값 in enumerate(리스트명):
        수행할 코드

a = [10,20,30]

for i in a:
    print(i)    # a 리스트의 값만 출력

print()

for item in enumerate(['가위','바위','보']):
    print(item)

print()

for index, value in enumerate(['가위','바위','보']):
    print(index,value)
                            
print()

for index, value in enumerate(a,start = 1):     # 인덱스 시작번호를 1로 정한다.
    print(f'{index}번째 : {value}')

print('--------------------')

# len() : 길이 (항목 수)

li = ['a','b','c','d']
print(len(li))

d = {'a' : 'apple', 'b' : 'banana'}
print(len(d))

print(len(range(10)))   # 0~9
print(len(range(1,10))) # 1~9

======================실행 결과======================
10
20
30

(0, '가위')
(1, '바위')
(2, '보')

0 가위
1 바위
2 보

1번째 : 10
2번째 : 20
3번째 : 30
--------------------
4
2
10
9


# ex) 총점과 평균 구하기

sc = [70, 60, 55, 75, 95]   # 학생 점수 리스트
total = 0   # 총점을 0으로 초기화

for i, v in enumerate(sc, start=1):
    print(f'{i}번째 학생의 점수 : {v}')
    total += v

print(f'총점 : {total} 점')

avg = total // len(sc)  # // 하면 소수점 없음
print(f'평균 : {avg} 점')

======================실행 결과======================
1번째 학생의 점수 : 70
2번째 학생의 점수 : 60
3번째 학생의 점수 : 55
4번째 학생의 점수 : 75
5번째 학생의 점수 : 95
총점 : 355 점
평균 : 71 점


# sorted() : 정렬할때 쓰는 함수
my_list = [6, 3, 1, 2, 5, 4]
sorted_list = sorted(my_list)
reverse_list = sorted(my_list, reverse = True)
print('원본 :', my_list)
print('정렬 후 (오름차순) :',sorted_list)
print('정렬 후 (내림차순) :',reverse_list)
print('------------------')

# zip() : 튜플로 묶어준다  for 문에서만 사용 가능
names = ['james', 'emily', 'amanda']
sc = [60, 70, 80]

for student in zip(names,sc):
    print(student)

print()

for name, score in zip(names,sc):
    print('{}의 점수는 {} 점 입니다.'.format(name,score))

======================실행 결과======================
원본 : [6, 3, 1, 2, 5, 4]
정렬 후 (오름차순) : [1, 2, 3, 4, 5, 6]
정렬 후 (내림차순) : [6, 5, 4, 3, 2, 1]
------------------
('james', 60)
('emily', 70)
('amanda', 80)

james의 점수는 60 점 입니다.
emily의 점수는 70 점 입니다.
amanda의 점수는 80 점 입니다.

# 159p)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,30,31]
for m,d in enumerate(months, start = 1):
    print(f'{m}월은 {d}일 까지 있다')

======================실행 결과======================
1월은 31일 까지 있다
2월은 28일 까지 있다
3월은 31일 까지 있다
4월은 30일 까지 있다
5월은 31일 까지 있다
6월은 30일 까지 있다
7월은 31일 까지 있다
8월은 31일 까지 있다
9월은 30일 까지 있다
10월은 31일 까지 있다
11월은 30일 까지 있다
12월은 31일 까지 있다


# 메소드

## 문자열 메소드

# count() : 특정 문자열의 개수를 파악
s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
print(s.count('기린'))

s = 'best of best'
print(s.count('best', 5))   # 5번째 부터 best 문자열을 찾아라
print(s.count('best',-7))   # -7번째 부터
print('---------------------')

# find(), index() : 특정 문자열 위치를 반환해줌
a = 'apple'
print(a.find('p'))  # 해당 인덱스 번호를 알려줌
print(a.find('s'))  # 없는 경우 -1 반환

print(s.find('best'))
print(s.find('best', 5))    # 지정한 인덱스부터 검색

print(a.index('p'))
print(a.index('x'))     # 없는 경우 에러 발생

======================실행 결과======================
4
1
1
---------------------
1
-1
0
8
1
Traceback (most recent call last):
  File "C:\python_평일\python_실습.py", line 24, in <module>
    print(a.index('x'))
ValueError: substring not found


# 대소문자 변환 메소드

s = 'BEST of best'
print(s.upper())    # 대문자
print(s.lower())    # 소문자
print(s.capitalize())   # 첫 글자만 대문자
print('--------------------')

# join() : 합치기

a = '-'.join('python')
print(a)

b = '+'.join(['a','b','c','d'])
print(b)

c = ''.join(['x','y','z'])
print(c)

d = ''.join({'a' : 'apple', 'b' : 'banana'})    # key만 사용
print(d)

print('--------------------')

# split() : 나누기 (리스트 형식으로)

a = 'Life is too short'
print(a.split())    # 공백을 기준으로 나눈다

b = '010-1234-5678'
print(b.split('-'))     # - 을 기준으로 나눈다

c = '제임스,25,남,서울'
print(c.split(','))     # , 을 기준으로 나눈다

print('--------------------')

# replace() : 바꾸기

print(a.replace('Life','Leg'))

print(b.replace('-',''))

# strip() : 불필요한 문자열을 제거

a = '     apple'
print(a)
print(len(a))

b = a.lstrip()  # 왼쪽 공백 제거, rstrip() : 오른쪽 공백 제거
print(b)
print(len(b))

c = '<head<'
print(c.strip('<')) # 양쪽의 < 문자 제거

======================실행 결과======================
BEST OF BEST
best of best
Best of best
--------------------
p-y-t-h-o-n
a+b+c+d
xyz
ab
--------------------
['Life', 'is', 'too', 'short']
['010', '1234', '5678']
['제임스', '25', '남', '서울']
--------------------
Leg is too short
01012345678
     apple
10
apple
5
head


# 173p)
## my sol.
while 1:
    
    num1 = input('주민등록번호를 입력하세요 : ')

    if num1[6] != '-':
        print('하이폰의 위치가 잘못되었습니다. 다시 입력해주세요.')
    else:
        bd = num1.split('-')
        break
print('생년월일은 {} 입니다'.format(bd[0]))


## book sol.

while 1:
    p = input('하이폰을 포함하여 주민등록번호를 입력하세요 : ')
    if p.find('-') != 6:
        print('하이폰의 위치가 잘못되었습니다.')
        continue    # 반복문의 처음으로 이동
    birthday = p.split('-')[0]  # '-'을 기준으로 분리
                                # 0번 인덱스 값을 birthday 에 담음
    print('생년월일은 {} 입니다.'.format(birthday))
    break

======================실행 결과======================
주민등록번호를 입력하세요 : 96021-169215
하이폰의 위치가 잘못되었습니다. 다시 입력해주세요.
주민등록번호를 입력하세요 : 960217-1693216
생년월일은 960217 입니다


# 리스트 메소드

# extend() : 확장
my_list = ['apple', 'banana']
my_list.extend(['cherry', 'mango']) # 2개이상을 추가 할 때 
print(my_list)

# remove() : 특정 값을 제거
my_list.remove('cherry')
print(my_list)

# clear() : 모든 값을 제거
my_list.clear()
print(my_list)

======================실행 결과======================
['apple', 'banana', 'cherry', 'mango']
['apple', 'banana', 'mango']
[]


# 177p)

a_list = ['above', 'cookie', 'app', 'about', 'admin', 'bisket', 'apple', 'april']

for i, item in enumerate(a_list):
    if item.find('a') == -1:
        print('{} 제거됩니다.'.format(a_list.pop(i)))    # i번째 값을 꺼내어서 제거
        
print(a_list)    

cookie 제거됩니다.
bisket 제거됩니다.
['above', 'app', 'about', 'admin', 'apple', 'april']


# 세트 메소드

s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

print('세트 s1 :', s1)
print('세트 s2 :', s2)

# 교집합

print(s1 & s2)
print(s1.intersection(s2))

# 합집합

print(s1 | s2)
print(s1.union(s2))

# 차집합

print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))

======================실행 결과======================
세트 s1 : {1, 2, 3, 4, 5, 6}
세트 s2 : {4, 5, 6, 7, 8, 9}
{4, 5, 6}
{4, 5, 6}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{1, 2, 3}
{1, 2, 3}
{8, 9, 7}
{8, 9, 7}


















