### 선형 리스트의 간단 구현 ###

katok = ['다현', '정연', '쯔위', '사나', '지효']
print(katok)

# 데이터 삽입 : 끝에 삽입
katok.append(None)   # 빈 칸 삽입
print(katok)
katok[5] = '모모'
print(katok)

# 데이터 삽입 : 중간에 삽입
katok.append(None)
print(katok)
katok[6] = katok[5]  # 5번 값을 6번 자리에 넣어라.
print(katok)
katok[5] = None
print(katok)
katok[5] = katok[4]
katok[4] = None
print(katok)
katok[4] = katok[3]
katok[3] = None
print(katok)
katok[3] = '미나'
print(katok)

# 데이터 삭제 : 중간 삭제
katok[4] = None
print(katok)
katok[4] = katok[5]
katok[5] = None
print(katok)
katok[5] = katok[6]
katok[6] = None
print(katok)
del(katok[6])
print(katok)