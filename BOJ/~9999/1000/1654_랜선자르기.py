
K,N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

start = 1 
end = max(lst)

while start <= end:
    middle = (start + end) // 2
    cnt = 0
    for i in lst:
        res = i // middle
        cnt += res

    if cnt >= N:  # 목표값보다 크다면 start 바꿔주기
        start = middle + 1

    else:
        end = middle - 1

print(end)