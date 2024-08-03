from sys import stdin

def func(n): # N! 함수
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

T = int(stdin.readline())
for _ in range(T):
    N,M = map(int, stdin.readline().split()) # mCn 하면 되는 문제임
    k = (func(M) // (func(N) * func(M-N))) # mCn = m! // (n! * (m-n)!)
    print(k)
