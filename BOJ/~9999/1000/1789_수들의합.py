from sys import stdin

S = int(stdin.readline())
res = 0
N=0
for i in range(1, S+1):
    res += i
    N +=1
    if res > S:
        N -=1  # s보다 커지기 전이.. 정답이니께..
        break

print(N)