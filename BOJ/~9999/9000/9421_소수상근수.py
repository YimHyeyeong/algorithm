from sys import stdin

def primes(n): # 소수를 반환하는 함수(에라토스테네스의 체)
    lst = [1, 1] + [0] * (n - 1)
    prime = []

    for i in range(2, n + 1):
        if not lst[i]:
            prime.append(i)
            for j in range(2*i, n+1, i): # i의 배수 모두를 소수가 아님으로 표시
                lst[j] = 1
    return prime

def func(n): # 상근수를 확인하는 함수
    visited = []
    while True:
        q = str(n)
        n = 0
        for k in q:
            n += int(k) ** 2

        if n == 1: # 1이 된다면 상근수
            return True

        if n in visited: # 또 다시 같은 수가 나온다면 상근수가 아님
            return False
        else:
            visited.append(n)

N = int(stdin.readline())


p_lst = primes(N)
for c in p_lst:
    if func(c):
        print(c)


