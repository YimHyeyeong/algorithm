N = int(input())

arr = [0] * 1000001

arr[1] = 1
arr[2] = 2

for i in range(3, N+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 15746  # n-2에 00 타일을 붙이고 n-1에 1 타일을 분이면 n

print(arr[N])