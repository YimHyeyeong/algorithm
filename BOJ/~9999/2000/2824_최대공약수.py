from sys import stdin
import math

N= int(stdin.readline())
N_list = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))

A = 1
for i in N_list:
    A *= i

B = 1
for j in M_list:
    B *= j

k = math.gcd(A,B)
if len(str(k)) > 9:
    print(str(k)[-9:])

else:
    print(k)
