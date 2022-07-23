# 내 풀이
money = int(input("금액 N원을 입력하세요 : "))
count = 0
rech = [500,100,50,10]
#
# for i in rech:
#     while 1:
#         if money >= i:
#             money = money - i
#             count +=1
#         else:
#             break
#
# print(f'횟수는 : {count}이다')

# 그리디 풀이

array = [500,100,50,10]
cnt = 0
for coin in array:
    cnt += money // coin    # 해당 화폐로 거슬러 줄수있는 동전의 개수 세기
    money %= coin

print(cnt)