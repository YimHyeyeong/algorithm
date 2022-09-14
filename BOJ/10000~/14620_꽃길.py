from sys import stdin

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def check(r, c): # r,c 좌표에 꽃을 심어도 되는지 확인하는 함수
    for i in range(5): #  0,0도 같이 확인
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            continue
        else:
            return False # 하나라도 안되면 리턴
    return True

# 최솟값을 구하는 함수
def func(n, cnt):
    global res

    if n == 3: # 3개의 꽃을 모두 다 심으면
        if cnt < res:
            res = cnt # 더 작은 값을 리턴
        return

    for i in range(1, N-1): 
        for j in range(1, N-1):

            if check(i,j): # 꽃을 심을 수 있으면
                ans = 0 # 땅의 값어치 저장
                for q in range(5):
                    nr = i + dr[q]
                    nc = j + dc[q]
                    visited[nr][nc] = 1 # 방문 표시
                    ans += arr[nr][nc] 

                func(n+1, cnt + ans)

                # 다시 방문 표시 풀어주기 
                for k in range(5):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    visited[nr][nc] = 0

N = int(stdin.readline())

arr = [list(map(int,stdin.readline().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

res = 21e8

func(0,0)
print(res)