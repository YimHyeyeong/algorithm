from sys import stdin

lst = stdin.readline().rstrip()
word = stdin.readline().rstrip()

k = 0
cnt = 0
while k <= len(lst):
    if lst[k: k+len(word)]== word:
        cnt += 1
        k += len(word)
    else:
        k += 1
print(cnt)
