N = int(input())
diff = []

for i in range(N):
    a1, b1 = map(int, input().split())
    diff.append(a1 - b1)

# set_diff = list(set(diff))
#
# k = []
#
# for i in set_diff:
#     k.append(diff.count(i))
#
# if max(k) != min(k):
#     N = 1
#
# if N == 1 or len(set_diff) % 2 == 1:
#     print(1)
#     exit()
#
# while len(set_diff) > 2:
#     set_diff.remove(min(set_diff))
#     set_diff.remove(max(set_diff))
#
# print(abs(set_diff[0] - set_diff[1]) + 1)

if N%2 == 1 :
    print(1)
    exit()

while len(diff)>2:
    diff.remove(max(diff))
    diff.remove(min(diff))

print(abs(diff[0]-diff[1])+1)