# csv 모듈로 CSV 파일 생성하기

import csv  # csv 파일을 쉽게 관리하기 위한 모듈을 불러온다.

with open('차량관리.csv','w', newline='') as file:  # 불필요한 라인을 추가하지 못하도록 설정
    csv_maker = csv.writer(file, delimiter = ',',quotechar ='"')   # 쓰기 객체 생성
    # delimiter: 각 인자 사이에 문자삽입
    # delimiter: csv파일이 뭘로 나누어져있는지
    # quotechar : 날짜/시간 데이터가 있는 문자열''안에도 ,(콤마,쉼표)가 있는데,
    #             일반적으로 콤마는 컬럼을 나누기 위해 쓰이지만 (delimiter = ',')
    #             이 쉼표는 컬럼을 나누기 위한것으로 들어간 것이 아니기 때문에
    #             콤마가 데이터로써 들어갔다고 표시하기위해 quotechar로 묶어줌.
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00']) # 한 줄씩 쓰기
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])

print('차량관리.csv 파일이 생성되었습니다.')

======================실행 결과======================
차량관리.csv 파일이 생성되었습니다.

# csv 모듈로 CSV 파일 읽기

import csv

with open('차량관리.csv','r', newline = '') as file:
    csv_reader = csv.reader(file, delimiter = ',', quotechar = '"') # 읽기 객체 생성
    # quotechar은 묶여져있는 string을 처리할 때 사용된다. 무엇으로 감싸져있는지.
    for line in csv_reader:
        print(line)

======================실행 결과======================
['1', '08러1234', '2020-10-20,14:00']
['2', '25다1234', '2020-10-20,14:10']
['3', '28하1234', '2020-10-20,14:20']


# JSON 파일 쓰기 (생성)

import json

dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [175.5, 70.5]
    },
    {
        'name' : 'alice',
        'age' : 21,
        'spec' : [168.5, 60.5]
    }
]

json_string = json.dumps(dict_list)     # json으로 인코딩한다.

with open('dictlist.json','w') as file:
    file.write(json_string)     # json으로 인코딩 한 내용을 json 파일에 쓴다.

print('dictlist.json 파일이 생성되었습니다.')

======================실행 결과======================
dictlist.json 파일이 생성되었습니다.


# JSON 파일 읽기

import json

with open('dictlist.json','r') as file:
    json_reader = file.read()   # 파일 전체를 읽어서  json_reader에 저장
    dict_list = json.loads(json_reader) # 파이썬으로 인코딩

print(dict_list)

for dic in dict_list:
    print('이름 : {}'.format(dic['name']))
    print('나이 : {}'.format(dic['age']))
    print('키 : {}'.format(dic['spec'][0]))
    print('몸무게 : {}'.format(dic['spec'][1]))
    print()

======================실행 결과======================
[{'name': 'james', 'age': 20, 'spec': [175.5, 70.5]}, {'name': 'alice', 'age': 21, 'spec': [168.5, 60.5]}]
이름 : james
나이 : 20
키 : 175.5
몸무게 : 70.5

이름 : alice
나이 : 21
키 : 168.5
몸무게 : 60.5


# 예외 처리

## 예외 종류

# SyntaxError : 잘못된 문법

    ex)
    '''
    print('test)
    print('hello'')
    '''
    
# NameError : 참조 변수 없음

    ex)
    a = 10
    b = 15
    print(c)

# ZeroDivisionError : 0 나누기 에러

    ex)
    print(10/0)

# IndexError : 인덱스 범위 오버

    x = [1, 2, 3]
    print(x[3])

# KeyError : 잘못된 key

    dic = {'name' : '홍길동',
           'age' : 20}
    print(dic['hobby'])     # 에러 발생
    print(dic.get('hobby')) # 에러 안나고 None을 반환

# ValueError : 참조 값이 없을 때

    x = [1, 5, 9]
    x.remove(100)

# TypeError : 자료형에 맞지 않는 연산을 수행할 경우

    x = [1,2]   # 리스트
    y = (1,2)   # 튜플
    z = 'test'  # 문자열
    print(x+y)  # 서로 다른 자료형이기 때문에 성립 안됨
    print(y+z)
    print(x+z)


# 모든 예외를 처리하는 방식 (try~except)

try:
    num = int(input('정수를 입력하세요 : ')) # 예외가 발생할 가능성이 있는 코드
    print('원의 반지름 :', num)
    print('원의 둘레 :', num*3.14*2)
    print('원의 넓이 :', num*num*3.14)

except:
    print('정수를 입력하지 않았습니다.')    # 정수를 입력하지 않으면 에러가 뜨지않고 이 메시지 출력

======================실행 결과======================
정수를 입력하세요 : 3
원의 반지름 : 3
원의 둘레 : 18.84
원의 넓이 : 28.26

정수를 입력하세요 : 1.5
정수를 입력하지 않았습니다.


# 297p)

try:
    height = input('키를 입력하세요 : ') # 문자열 형태로 입력받음
    height = round(heigh)    # 반올림 (예외 발생)
    print('입력하신 키는 {}cm로 처리됩니다.'.format(height))
except:
    print('예외가 발생했습니다.')

======================실행 결과======================
키를 입력하세요 : 180
예외가 발생했습니다.


# 특정 예외만 처리하는 방식

try:
    a = int(input('제수를 입력하세요 : '))
    b = int(input('피제수를 입력하세요 : '))
    print('{}/{} = {}'.format(a, b, a / b))
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except Exception:
    print('알 수 없는 예외가 발생했습니다.')

======================실행 결과======================
제수를 입력하세요 : 5
피제수를 입력하세요 : 3
5/3 = 1.6666666666666667


# 예외 메시지 처리하기

a = [10, 20, 30, 40, 50]

try:
    print(a[10])
except IndexError as e:
    print(e)

======================실행 결과======================
list index out of range
 

# else문과 finally문

    finally 구문 : 예외 처리 구문에서 가장 마지막에 사용할 수 있는 구문
                   예외 발생 여부와 관계없이 무조건 실행해야 할 경우에 사용

    else 구문 : 예외 발생하지 않고 정상적으로 처리될 때 실행되는 구문

    try 구문은 단독으로는 사용할 수 업으며,
    반드시 except 또는 finally 구문과 함께 사용해야 함
    else 구문은 반드시 except 뒤에 사용


# ex)

try:
    num = int(input('정수를 입력하세요 : '))
except:
    print('정수를 입력하지 않았습니다.')
else:
    print('원의 반지름 :',num)   # 예외가 발생하지 않았을 때 실행(정상적으로 작동)
    print('원의 둘레 :',num*3.14*2)
    print('원의 넓이 :',num*num*3.14)
finally:
    print('일단 프로그램이 끝이 났습니다.')  # 무조건 실행

======================실행 결과======================
정수를 입력하세요 : a
정수를 입력하지 않았습니다.
일단 프로그램이 끝이 났습니다.

# 301p)

try:
    filename = input('열고자 하는 파일명을 입력하세요 : ') # 예외 발생 가능성이 있는 코드
    file = open(filename, 'rt')     # 파일 열기
except FileNotFoundError:   # 예외가 발생했을 때 실행
    print('{} 파일이 존재하지 않습니다.'.format(filename))
else:   # 예외가 발생하지 않았을 때 실행 (정상적일 때)
    buffer = file.read()
    print(buffer, end = '')
    print()
    file.close()    # 파일 닫기
finally:    # 무조건 실행
    print('프로그램을 종료합니다.')

======================실행 결과======================
열고자 하는 파일명을 입력하세요 : 차량관리.csv
1,08러1234,"2020-10-20,14:00"
2,25다1234,"2020-10-20,14:10"
3,28하1234,"2020-10-20,14:20"

프로그램을 종료합니다.


# 강제로 예외 발생시키기 (raise)

    예외를 강제로 발생시킴
    프로그램 개발 단계에서 아직 구현되지 않은 부분에
    일부러 예외를 발생시켜 잊어버리지 않도록 하는 경우에 활용

# ex)

num = int(input('정수를 입력하세요 : '))

if num > 0:
    raise '아직 구현되지 않은 코드입니다.'
else:
    print('0 또는 음수입니다.')

======================실행 결과======================
정수를 입력하세요 : 2
Traceback (most recent call last):
  File "C:\python_평일\python_실습.py", line 8, in <module>
    raise '아직 구현되지 않은 코드입니다.'
TypeError: exceptions must derive from BaseException


# 304p)

try:
    score = int(input('점수를 입력하세요 : '))
    if score < 0 or score > 100:    # 점수 범위를 벗어난다면
        raise Exception('점수는 0~100 사이입니다.')
except Exception as e:
    print(e)    # 예외 메세지 출력
else:
    if score >= 80:
        print('{}점은 합격입니다.'.format(score))
    else:
        print('{}점은 불합격입니다.'.format(score))

======================실행 결과======================
점수를 입력하세요 : 82
82점은 합격입니다.


## 사용자 예외 클래스

# 305p)

class NameError(Exception):     # Exception 클래스를 상속받음
    def __init__(self, message):
        super().__init__(message)

try:
    name = input('이름을 입력하세요 : ')
    if len(name) < 2 or len(name) > 6:
        raise NameError('이름은 2자에서 6자 사이로 입력해주세요.')
except NameError as e:
    print(e)
else:
    print('입력된 이름은 {}입니다.'.format(name))

======================실행 결과======================
이름을 입력하세요 : 홍
이름은 2자에서 6자 사이로 입력해주세요.

## pass문

    예외 발생 시 바로 처리해야하지만, 크게 중요한 부분이 아닐 경우
    프로그램의 강제 종료를 막는 목적으로 pass 구문을 사용

    <형식>
    try:
        예외가 발생할 가능성이 있는 코드
    except:
        pass

# ex)

list_a = ['52', '123', '29', '파이썬', '111']

list_num = []   # 숫자만 담을 빈 리스트 생성

for i in list_a:    # list_a에 있는 값들을 하나씩 꺼내어 반복
    try:
        int(i)  # 정수형인 숫자로 변환
        list_num.append(i)  # 예외없이 통과한 값만 list_num에 추가
    except:
        pass    # 예외 발생 시 그냥 넘어감
print(list_num)

======================실행 결과======================
['52', '123', '29', '111']






