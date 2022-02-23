T = int(input())

arr = [0] * 101

arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

for i in range(6, 101):
    arr[i] = arr[i-2] + arr[i-3]  # [i-1] + [i-5] 한 것도 같음


for j in range(T):
    N = int(input())
    print(arr[N])
