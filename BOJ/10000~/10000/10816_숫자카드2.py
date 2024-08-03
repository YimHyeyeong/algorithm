from sys import stdin

N = int(stdin.readline())

n_list = list(map(int, stdin.readline().split()))

M = int(stdin.readline())
m_list = list(map(int, stdin.readline().split()))

dic = {}

for i in n_list:
    if  i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for j in m_list:
    if j in dic:
        print(dic[j], end= ' ')
    else:
        print(0, end= ' ')