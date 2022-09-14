from sys import stdin

T = int(stdin.readline())

# 결론적으로 총 진입/이탈 횟수가 추가되는 경우는
# 출발점이나 도착점이 행성 내부에 위치한 경우 (출발점과 행성 중심과의 거리가 행성 반지름보다 작은 경우) 이다.
# 단, 출발점과 도착점이 모두 행성 내부에 위치해 있다면 (행성 중심과의 거리가 '모두' 행성의 반지름보다 작은 경우)
# 특정 행성을 들릴 필요가 없기 때문에 총 진입/이탈 횟수는 0이 된다.

for _ in range(T):
    x1, y1, x2,y2 = map(int, stdin.readline().split())
    n = int(stdin.readline())
    cnt = 0
    for _ in range(n):
        cx,cy,r = map(int, stdin.readline().split())

        distance1 = (x1-cx) ** 2 + (y1-cy) ** 2 # 출발점과 행성 중심점과의 거리
        distance2 = (x2-cx) ** 2 + (y2-cy) ** 2 # 도착점과 행성 중심점과의 거리
        cr = r ** 2 

        if cr > distance1 and cr > distance2: # 출발점, 도착 점 모두 한 행성 내부에 있는 경우
            continue
        elif cr > distance1: # 하나의 점만이 행성 내부에 있는 경우
            cnt +=1
        elif cr > distance2:
            cnt += 1

    print(cnt)
