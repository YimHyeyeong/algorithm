# 1
from sys import stdin

N = int(stdin.readline())
lst = []
for _ in range(N):
    age, name = stdin.readline().split()
    lst.append((int(age), name))

a = sorted(lst, key=lambda x: x[0])

for i in a:
    print(*i)


# 2

N = int(input())

lst = []

for _ in range(N):
    age, name = input().split()
    age = int(age)
    lst.append([age,name])

lst.sort(key=lambda x: x[0])

for i in lst:
    print(*i)