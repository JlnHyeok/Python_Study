n = int(input())
book = [None for _ in range(n)]

for i in range(n):
    book[i] = input()
book = sorted(book)
cnt_list = [0 for _ in range(len(book))]
i = 0
while i<len(book)-1:
    cnt = book.count(book[i])
    cnt_list[i]=(cnt)
    i += cnt

print(book[cnt_list.index(max(cnt_list))])
# print(book[cnt_list.index(max(cnt_list))])
# print(cnt_list)