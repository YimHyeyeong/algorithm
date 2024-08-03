from sys import stdin

N, M = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))

start = 1
end = max(lst)
while start <= end:
    middle = (start + end) // 2
    cnt = 0
    for i in lst:
        if i >= middle:  # middle 보다 작으면 나무는 잘리지 않음
            cnt += i - middle

    if cnt >= M:
        start = middle + 1
    else:
        end = middle -1

print(end)

