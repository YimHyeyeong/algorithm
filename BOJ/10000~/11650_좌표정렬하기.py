import sys
N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

# 람다식, 정렬 기준을 정해줌
lst.sort(key=lambda x: (x[0], x[1]))

for i in lst:
    print(*i)