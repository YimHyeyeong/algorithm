from sys import stdin

N = int(stdin.readline())
V = [0] * (N+1)

for i in range(2, N+1):
    V[i] = V[i-1] +1  # 만약 i가 2나 3으로 딱 떨어지지 않는다면 -1을 하면 이전의 숫자와 같아지기 때문에 횟수를 +1 하기만 하면됨

    # 여기서 if elif else를 사용하면 안된다. if만 이용해야 세 연산을 다 거칠 수 있다,
    if i % 3 == 0:
        V[i] = min(V[i], V[i//3] +1) ## 1을 더하는 것은 V는 결과가 아닌 계산한 횟수를 저장하는 것 이기 때문이다.
    if i % 2 == 0:
        V[i] = min(V[i], V[i//2] +1)
print(V[N])

# 참고 링크: https://seongonion.tistory.com/40