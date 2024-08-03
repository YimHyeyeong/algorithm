from sys import stdin

# 연속되는 구간 체크하는 함수
def max_count(arr):
    res = 0

    # 가로
    for i in range(N):
        cnt = 0
        for j in range(1,N):
            # 연속된다면
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            # 끊기면 초기화
            else:
                if res < cnt:
                    res = cnt
                cnt = 0
        if res < cnt:
            res = cnt

    # 세로
    for k in range(N):
        cnt = 0
        for q in range(1, N):
            # 연속된다면
            if arr[q][k] == arr[q-1][k]:
                cnt += 1
            # 끊기면 초기화
            else:
                if res < cnt:
                    res = cnt
                cnt = 0
        if res < cnt:
            res = cnt

    return res + 1

N = int(stdin.readline())
Bomboni = [list(stdin.readline().rstrip()) for _ in range(N)]

ans = 0

# N의 길이 최대가 50뿐이기 때문에 하나씩 다 돌아보면 됨
# 가로로 돌기
for i in range(N):
    for j in range(1,N):
        if Bomboni[i][j] != Bomboni[i][j-1]:
            #사탕색이 다른 인접한 칸 서로 바꿔주기
            Bomboni[i][j], Bomboni[i][j-1] = Bomboni[i][j-1], Bomboni[i][j]
            max_CNT = max_count(Bomboni)
            if ans < max_CNT:
                ans = max_CNT
        # 다시 원상복구
        Bomboni[i][j], Bomboni[i][j - 1] = Bomboni[i][j - 1], Bomboni[i][j]

# 세로로 돌기
for k in range(N):
    for q in range(1, N):
        if Bomboni[q][k] != Bomboni[q-1][k]:
            #사탕색이 다른 인접한 칸 서로 바꿔주기
            Bomboni[q][k], Bomboni[q-1][k] = Bomboni[q-1][k], Bomboni[q][k]
            max_CNT = max_count(Bomboni)
            if ans < max_CNT:
                ans = max_CNT
        # 다시 원상복구
        Bomboni[q][k], Bomboni[q - 1][k] = Bomboni[q - 1][k], Bomboni[q][k]

print(ans)

