from sys import stdin
from itertools import permutations

lst = [stdin.readline().rstrip() for _ in range(6)]

def check(a,b,c):
    d = a[0] + b[0] + c[0]
    e = a[1] + b[1] + c[1]
    f = a[2] + b[2] + c[2]
    if sorted([a,b,c,d,e,f]) == lst: # sort() 하면 None 리턴되서 안됨
        return True
    return False

for i in permutations(lst,3):
    w1, w2, w3 = i
    if check(w1,w2,w3):
        print(w1)
        print(w2)
        print(w3)
        exit()
print(0)