from sys import stdin
N,M = map(int,stdin.readline().split())

lst_n = list(stdin.readline() for _ in range(N))
cnt = 0
for _ in range(M):
    m_str = stdin.readline()
    if m_str in lst_n:
        cnt += 1

print(cnt)