from sys import stdin
from itertools import product # 중복순열, 비밀번호이니까 순서상관있음 고로 순열


n, m = map(int, stdin.readline().split())

lst = list(map(int, stdin.readline().split()))

cmb = [i for i in range(0, 10)]

all_cnt = 0
cnt = 0
for i in product(cmb, repeat=n): 
    all_cnt += 1
    for j in lst:
        if j not in i: # 하나라도 선견지명 숫자가 없다면 카운드
            cnt += 1
            break

print(all_cnt - cnt) # 모든 순열에서 선견지명이 포함되지 않은 순열을 빼면 선견지명이 포함된 순열의 개수가 나옴
