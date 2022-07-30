# 중복없는 순열 만들기

[1]
def func(n,m,k):
    if n == k :
        print(*p)
    else:
        for i in range(m):
            if u[i] == 0:   # 중복방지
                u[i] = 1    # 중복체크
                p[k] = arr[i]  
                func(n,m,k+1)   # 다음 칸(레벨)으로 이동
                u[i] = 0     # 중복체크 초기화

 


N, M = map(int, input().split())
p = [0] * M

arr = []
for i in range(1,N+1):
    arr.append(i)

u = [0] * N  # 중복방지

func(M,N,0)

#############################
[2]
def func(level):
    if level == M : # 0 1 2 3 ... M-1
        for i in range(M):
            print(path[i], end = ' ')
        print()
        return

    for i in range(1, N + 1) : # 현재 선택할 수는 i
        if used[i] == 1 : continue
        used[i] = 1
        path[level] = i
        func(level + 1)
        path[level] = 0
        used[i] = 0



N,M = map(int ,input().split())
path = [0] * 8
used = [0] * 9 # 1 2 3 4 ... 8 index 를 이용해서 체크

func(0)