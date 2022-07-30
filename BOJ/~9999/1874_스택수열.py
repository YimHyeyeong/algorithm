n = int(input())  # 1~n 까지의 숫자를 이용해 문제의 수열을 만듦

lst = [] # 수열 저장
res = [] # 결과 저장
temp = True # 수열이 가능한지 판단
cnt = 1 

for _ in range(n):
    num = int(input()) 

    while cnt <= num: # 1~ num를 모조리 lst에 push
        lst.append(cnt)
        cnt += 1
        res.append('+')

    if lst[-1] == num:  # 마지막 숫자가 num과 같다면 수열 ok
        lst.pop()
        res.append('-')

    else:  # 안된다면 no 출력
        temp = False
        break

if temp:
    for i in res:
        print(i)
else:
    print('NO')

