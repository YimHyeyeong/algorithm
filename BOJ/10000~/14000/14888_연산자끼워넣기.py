from sys import stdin
from itertools import permutations

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
lst = list(map(int,stdin.readline().split()))

lst1 = ['+', '-', '*', '/']
lst2 = [] # 연산자 넣는 배열

for i in range(len(lst)): 
    for j in range(lst[i]): # 연산자 수만큼 돌리기
        lst2.append(lst1[i])

max_num = -21e8 # 최댓값
min_num = 21e8 # 최솟값

for permutation in permutations(lst2, N-1): # 연산자로 가능한 수열 만들기
    res = nums[0] # 숫자 중 첫번째값
    for k in range(1,N):
        if permutation[k-1] == '+': # 숫자는 2번째 숫자, 연산자는 첫 번째 연산자
            res += nums[k]
        elif permutation[k-1] == '-':
            res -= nums[k]
        elif permutation[k-1] == '*':
            res *= nums[k]
        elif permutation[k-1] == '/':
            if res > 0: # 나눠지는 수가 양수일 경우
                res //= nums[k] # 그냥 몫만 취함
            else: # 음수일 경우
                res = -res // nums[k] # 나눠지는 음수 값을 양수로 바꾸고
                res *= -1 # 다시 몫을 음수로 함

    if res > max_num: # 최댓값일 경우
        max_num = res
    if res < min_num: # elif 쓰면 숫자가 2개뿐일 경우에 안됨
        min_num = res
print(max_num)
print(min_num)

