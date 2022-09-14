from sys import stdin

N = int(stdin.readline())
lst = [stdin.readline().rstrip() for _ in range(N)]

cnt = 0
for i in range(1,len(lst[0])+1):
    nums = []
    for j in lst:
        if j[-i:] in nums:
            break
        else:
            nums.append(j[-i:])
            if len(nums) == N:
                print(cnt+1)
                exit()
    cnt += 1

