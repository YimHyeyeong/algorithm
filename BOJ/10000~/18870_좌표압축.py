import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

sorted_lst = list(sorted(set(lst))) 

arr = {sorted_lst[i]: i for i in range(len(sorted_lst))}  # index 사용시 시간 초과

for j in lst:
    print(arr[j], end=' ')