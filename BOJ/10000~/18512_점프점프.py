from sys import stdin

x,y,p1,p2 = map(int, stdin.readline().split())

A = [p1]
B = [p2]

for i in range(100):
    a = A[i] + x
    b = B[i] + y
    A.append(a)
    B.append(b)
    if a in B or b in A:
        print(min(a,b))
        break
else:
    print(-1)
