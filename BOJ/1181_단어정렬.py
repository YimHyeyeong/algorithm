N = int(input())

set_lst = set(input() for _ in range(N))

lst = []
for i in set_lst:
    lst.append((len(i),i))

lst.sort(key=lambda x: (x[0], x[1]))

for j in lst:
    print(j[1])