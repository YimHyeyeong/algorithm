# sorted 사용
N = int(input())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)

b = sorted(lst)
for i in b:
    print(i)

# 버블 정렬
def func(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]

N = int(input())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)


func(lst)
for i in lst:
    print(i)
