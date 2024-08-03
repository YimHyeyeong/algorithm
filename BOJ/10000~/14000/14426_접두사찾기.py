from sys import stdin

N,M = map(int, stdin.readline().split())

N_list = [stdin.readline().rstrip() for _ in range(N)]
M_list = [stdin.readline().rstrip() for _ in range(M)]
cnt = 0
for i in M_list: # M_list 먼저 for 문을 돌려야함
    for j in N_list: # 아니면 N_list에서 다 돌면 끝나버려서 안됨. M_list 검사도 덜 하고 끝나버림
        if i == j[:len(i)] and len(i) <= len(j):
            cnt += 1
            break

print(cnt)