from sys import stdin

X,Y,W,S = map(int, stdin.readline().split())

res1 = (X+Y) * W  # 평행 이동만 하는 경우

# 대각선 이동하는 경우
if (X+Y) % 2: # 홀수의 경우 모두 다 대각선으로 이동할 수 없기 때문에 한 번 평행 이동해줘야 함
    res2 = (max(X,Y)-1) * S + W
else: # 짝수
    res2 = max(X,Y) * S

# 평행이동과 대각선이동을 혼합하는 경우
# 작은 숫자 만큼 대각선이동하고 나머지는 평행이동
res3 = (min(X,Y) * S) + ((max(X,Y) - min(X,Y)) * W)

print(min(res1,res2,res3))