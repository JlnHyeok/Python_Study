n = int(input())
book = [None for _ in range(n)]

for i in range(n):
    book[i] = input()
book = sorted(book)
book.append(None)
cnt_list = [0 for _ in range(len(book))]
i = 0
while book[i]:
    cnt = book.count(book[i])
    cnt_list[i]=(cnt)
    i += cnt

print(book[cnt_list.index(max(cnt_list))])
# print(book[cnt_list.index(max(cnt_list))])
# print(cnt_list)