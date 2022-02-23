lst = input().split('-') # 마이너스를 기준으로 분리

res = 0
for i in lst[0].split('+'): # 제일 앞의 수들을 더한 후
    res += int(i)

for j in lst[1:]:  # 그 뒤의 수들은 모조리 뺌
    for k in j.split('+'):
        res -= int(k)

print(res)