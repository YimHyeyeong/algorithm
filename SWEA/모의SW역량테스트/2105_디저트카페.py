dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def tour(r, c, line):
    visit = set()
    for i in range(4): # 네방향에 대해서 반복
        for _ in range(line[i]):
            r, c = r + dr[i], c + dc[i]
            if arr[r][c] in visit:
                return False
            visit.add(arr[r][c])
    return True

def check(w, h):
    # w, h 에 해당한는 사각형의 시작점을 모든 생성
    for r in range(0, N - w - h):
        for c in range(h, N - w):
            if tour(r, c, [w, h, w, h]):
                return True
    return False


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 모든 사각형 경로를 조사해야 된다.
    # 시작점 = (r, c), 이동거리 => w, h
    # 모든 간으한 w, h 를 생성 => l = w + h
    ans = -1
    for l in range(N - 1, 1, -1):       # 2 <= l <= N - 1
        for w in range(1, l):   # h = l - w
            if check(w, l - w):
                ans = l * 2
                break
        if ans != -1:
            break
    print(ans)