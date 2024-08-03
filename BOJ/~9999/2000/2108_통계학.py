import sys
from collections import Counter

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(lst)/len(lst)))

# 중앙값
lst.sort()
print(lst[len(lst)//2])

# 최빈값
count_lst = Counter(lst).most_common()
if len(count_lst) > 1:
    if count_lst[0][1] == count_lst[1][1]:
        print(count_lst[1][0])

    else:
        print(count_lst[0][0])

else:
    print(count_lst[0][0])

# 범위
print(lst[-1]-lst[0])



# Counter을 사용하지 않고 풀이
from sys import stdin

N = int(stdin.readline())
lst = [int(stdin.readline()) for _ in range(N)]

# 산술평균
print(round(sum(lst)/N))

# 중앙값
lst.sort()
print(lst[N//2])

# 최빈값
count_dic = {} # 개수만큼 저장
counts = 1
for i in range(1, N):
    if lst[i] == lst[i-1]: # 이전에 위치한 값과 같다면
        counts += 1
    else:
        if counts in count_dic:
            count_dic[counts].append(lst[i-1])
        else:
            count_dic[counts] = [lst[i-1]]
        counts = 1

    if i == N - 1: # 마지막 숫자 저장
        if counts in count_dic:
            count_dic[counts].append(lst[i])
        else:
            count_dic[counts] = [lst[i]]


if N == 1:
    print(*lst)
else:
    max_count = max(count_dic)
    count_dic[max_count].sort()
    if len(count_dic[max_count]) > 1:
        print(count_dic[max_count][1])
    else:
        print(count_dic[max_count][0])

# 범위
print(lst[-1]-lst[0])