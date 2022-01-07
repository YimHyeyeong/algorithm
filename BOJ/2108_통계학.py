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