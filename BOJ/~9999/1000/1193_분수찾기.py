from sys import stdin

X = int(stdin.readline())

n = 0 # 그 라인에서 가장 큰 숫자
line = 0 # 몇 번째 사선인지
while X > n:
    line += 1
    n += line

a = line - (n - X)
b = n - X + 1
if line % 2: # 홀수이면 왼쪽아래에서 오른쪽 위로
    print('{}/{}'.format(b,a))
else: # 짝수면  오른쪽 위에서 왼쪽 아래로
    print('{}/{}'.format(a,b))



