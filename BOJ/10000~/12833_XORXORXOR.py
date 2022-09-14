from sys import stdin

A, B,C = map(int, stdin.readline().split()) # 계속 해서 b로 XOR 하면 2가지 결과만 반복해서 계속 나옴
print(A^B if C % 2 else A)