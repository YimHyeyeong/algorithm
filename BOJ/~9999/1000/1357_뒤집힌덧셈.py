from sys import stdin


X, Y = stdin.readline().split()
res = int(X[::-1]) + int(Y[::-1])
print(int(str(res)[::-1]))