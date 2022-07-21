# 선형리스트의 일반 구현

## 전역 변수 선언 부분

katok = []
select = -1     # 1 : 생성, 2 : 삽입, 3 : 삭제, 4 : 종료

## 함수 선언 부분

# 선형 리스트 생성하는 함수

def add_data(friend):
    katok.append(None)
    kLen = len(katok)   # 개수
    katok[kLen-1] = friend

# 데이터를 삽입하는 함수

def insert_data(position, friend):
    if position < 0 or position > len(katok):   # 범위안에 있지 않다면
        print('데이터를 삽입할 범위를 벗어났습니다.')   # 오류 메세지 출력
        return  # 함수 종료

    katok.append(None)  # 빈 칸 추가
    kLen = len(katok)   # 배열의 현재 크기

    for i in range(kLen - 1, position, -1):     # 마지막 위치부터 삽입할 위치까지
        katok[i] = katok[i-1]   # 한칸씩 오른쪽으로 자리 이동
        katok[i-1] = None       # 빈칸으로 만들어준다.

    katok[position] = friend    # 지정한 위치에 데이터를 추가


# 데이터를 삭제하는 함수

def delete_data(position):
    if position < 0 or position >= len(katok):
        print('데이터를 삭제할 범위를 벗어났습니다.')
        return  # 함수 종료

    kLen = len(katok)
    katok[position] = None  # 데이터 삭제
    for i in range(position+1,kLen):
        katok[i-1] = katok[i]   # pos 자리에 pos+1 값을 넣는다 --> 한칸씩 왼쪽으로
        katok[i] = None

    del (katok[kLen-1])     # 맨 뒤의 빈칸을 삭제

# 메인코드 부분

if __name__ == '__main__':
    while select != 4:
        select = int(input('선택하세요(1:생성, 2:삽입, 3:삭제, 4:종료)-->'))
        if select == 1:
            data = input('생성할 데이터 -->')
            add_data(data)  # 생성함수 호출
            print(katok)
        elif select == 2:
            pos = int(input('삽입할 위치 -->'))
            data = input('삽입할 데이터 -->')
            insert_data(pos, data)  # 삽입함수 호출
            print(katok)

        elif select == 3:
            pos = int(input('삭제할 위치 -->'))
            delete_data(pos)    # 삭제함수 호출
            print(katok)

        elif select ==4:
            print(katok)
            break

        else:
            print('1~4 중 하나를 입력하세요.')
            continue