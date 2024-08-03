from sys import stdin

N = int(stdin.readline())
road = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))

res = 0
m = price[0]
for i in range(N-1):
    if m > price[i]: # 가장 작은 기름값 저장
        m = price[i] 
    res += m * road[i]

print(res)