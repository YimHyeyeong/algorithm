def func(key): # 이진검색
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if i == n_lst[middle]:
            return 1
        elif i > n_lst[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return 0

N = int(input())
n_lst = list(map(int,input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

n_lst.sort()
for i in m_lst:
    res = func(i)
    print(res)

