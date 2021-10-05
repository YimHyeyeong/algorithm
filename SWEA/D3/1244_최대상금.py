
# [1]
def func(cnt):
    global A
    if cnt == changes or cnt == length:  # cnt == length 안하니 런타임 에러뜸
        numbers = int(''.join(nums)) #리스트 -> 숫자

        if numbers > A:
            A = numbers

        return


    for i in range(length):
        for j in range(i+1, length):  # 비교를 위해 이중 
            nums[i], nums[j] = nums[j] , nums[i]
            func(cnt+1)
            nums[i], nums[j] = nums[j], nums[i]


tc = int(input())

for t in range(1,tc+1):
    A = -1
    num, change  = input().split()
    changes = int(change)
    nums = list(num)
    length = len(nums)
    func(0)
    print('#{} {}'.format(t, A))

#############
# [2]

def dfs(level):
    global max_num
    if level == N :
        #int(''.join(lst)) vs max_num
        max_num = max(int(''.join(lst)), max_num)
        return
    for y in range(len(lst)):
        for x in range(y + 1, len(lst)):
            lst[y], lst[x] = lst[x], lst[y]
            state = ''.join(lst) + "#" + str(level)
            if state in visited :  
                lst[y],lst[x] = lst[x],lst[y]
                continue # 교환상태 + level 을 이용
            visited.add(state)  # 방문?한 곳을 표시, 런타임에러 방지
            dfs(level + 1)
            lst[y], lst[x] = lst[x], lst[y]

T = int(input())
for tc in range(1, T + 1) :
    lst , N = input().split()
    lst = list(lst)
    N = int(N)
    max_num = -int(21e8)
    visited = set()
    dfs(0)
    print("#{} {}".format(tc, max_num))
