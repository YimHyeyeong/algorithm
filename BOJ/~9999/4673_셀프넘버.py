all_num_list = set(range(1,10001))
lst = set()

for i in all_num_list:
    k = sum(map(int, str(i)))
    lst.add(k+i)

res = all_num_list - lst
for j in sorted(res):
    print(j)