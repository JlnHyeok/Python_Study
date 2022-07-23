# 어떠한 수 n이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# 두번째 연산은 n이 k로 나누어 떨어질때만 선택할 수 있다.
# 1. n에서 1을 뺀다.
# 2. n릏 k로 나눈다.
# ex) n=17 , k=4 라고 한다면 n을 1로 만드는 최소횟수는 3번이다.

# # 내 풀이
# n = int(input("n을 입력하세요"))
# k = int(input("k을 입력하세요"))
# cnt = 0
# while 1:
#     if n % k == 0:
#         n/=k
#         cnt +=1
#
#     else:
#         n-=1
#         cnt +=1
#     if n==1:
#         break
#
# print(cnt)
#
# # 백준 풀이
n,k =map(int, input().split()) # n,k를 공백을 기준으로 구분하여 입력받기

result = 0

while 1:
    ## target 은 k로 나누어떨어지는 n에 가장 가까운 수(n이 k로 나누어 떨어질 때 까지 빼기)
    target = (n//k)*k
    result += n - target
    n = target
    # n이 k보다 작을때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break

    result += 1
    n //=k

# n이 1보다 크다면 1로 만들어주기 위해서 (마지막으로 남은 수에 대하여 1씩 빼기)
result += n-1
print(result)

# 1빼는 식을 한번에 처리