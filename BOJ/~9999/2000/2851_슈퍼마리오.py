from sys import stdin

lst = list(int(stdin.readline()) for _ in range(10))

cnt = 0
for i in range(len(lst)):
    k = sum(lst[:i+1])
    if abs(100-cnt) >= abs(100-k):
        cnt = k

print(cnt)
