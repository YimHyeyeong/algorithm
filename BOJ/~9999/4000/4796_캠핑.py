from sys import stdin
cnt = 0
while True:
    cnt += 1
    L, P, V = map(int, stdin.readline().split())
    if L == P == V == 0:
        break

    a = V // P
    b = V % P

    if b > L: # 남은 날짜가 연속해서 사용할 수 있는 날짜보다 클 때
        b = L

    print('Case {}: {}'.format(cnt, L*a + b))