import sys
N = int(sys.stdin.readline())
counts = [0] * 10001
for _ in range(N):
    counts[int(sys.stdin.readline())] += 1


for i in range(len(counts)):
    while counts[i] > 0:
        print(i)
        counts[i] -= 1