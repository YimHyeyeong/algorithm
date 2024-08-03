N = int(input())

lst = list(map(int, input().split()))

lst.sort()  # 오름차순정렬
res = 0
for i in range(N):
    for j in range(i+1):  # 앞에서부터 누적합 구함
        res += lst[j]

print(res)