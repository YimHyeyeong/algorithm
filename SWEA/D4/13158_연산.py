#[1] deque 사용시
from collections import deque

def bfs(n,m):
    que = deque() 
    visited = [0] * 1000001 # 재방문 방지
    visited[n] = 1 # 처음 값 방문 표시
    que.append((n,0))  # 처음 값 입력

    while que:
        num, cnt = que.popleft()
        if num == m:  # 찾는 값이면 리턴
            return cnt
        if 0<= num +1 <= 1000000 and visited[num+1] == 0 :
            visited[num+1] = 1
            que.append((num+1, cnt+1))
        if 0 <= num - 1 <= 1000000 and visited[num -1 ] == 0:
            visited[num - 1] = 1
            que.append((num - 1, cnt + 1))
        if 0 <= num *2  <= 1000000 and visited[num *2] == 0:
            visited[num * 2] = 1
            que.append((num * 2, cnt + 1))
        if 0 <= num - 10 <= 1000000 and visited[num - 10] == 0:
            visited[num - 10] = 1
            que.append((num - 10, cnt + 1))


tc = int(input())
for t in range(1,tc+1):
    N,M = map(int,input().split())
    print('#{} {}'.format(t,bfs(N,M)))
