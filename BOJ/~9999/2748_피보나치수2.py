from sys import stdin

def func(k):
    fibo = [0, 1]

    for i in range(2,k+1):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo[k]
n = int(stdin.readline())

print(func(n))