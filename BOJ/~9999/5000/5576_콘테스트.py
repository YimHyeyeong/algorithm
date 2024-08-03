from sys import stdin

W = list(int(stdin.readline()) for _ in range(10))
K = list(int(stdin.readline()) for _ in range(10))

W.sort()
K.sort()
print(sum(W[7:]), end=' ')
print(sum(K[7:]))