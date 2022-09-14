from sys import stdin
import math

A, B = map(int,stdin.readline().split())

print('1'* (math.gcd(A,B))) # 이 방법 외에는 메모리 초과