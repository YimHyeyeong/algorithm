from sys import stdin

N = int(stdin.readline())
lst = list(map(int,stdin.readline().split()))

for i in range(N-1, 0, -1):
    if lst[i] > lst[i-1]:
        for j in range(N-1, 0, -1):
            if lst[i-1] < lst[j]:
                lst[i-1], lst[j] = lst[j], lst[i-1]
                sort_lst = sorted(lst[i:])
                lst = lst[:i] + sort_lst
                print(*lst)
                exit()
print(-1)


# 1 4 3 2를 예시로 알고리즘을 알아본다.

 

# 뒤에서부터 순열을 비교하며, 뒷 값이 앞 값보다 큰 경우까지 반복한다. (3,2), (4,3)은 해당하지 않고, (1,4)가 해당된다. 
# 이 때, 1의 인덱스를 x라고 칭한다.
# 4의 인덱스는 y라고 한다.
# 다시 뒤에서부터 값을 비교하며 인덱스 x보다 큰 값이 있으면 그 값과 swap한다.
# 1과 2를 비교했고, 2가 크기 때문에 이 둘을 swap한다.
# y에 해당하는 인덱스부터 sort(오름차순정렬)를 한 뒤에 이어 붙인다.
# 4 3 1을 sort해서 1 3 4가 된다.
# 이어 붙이기 때문에 2 1 3 4가 된다.