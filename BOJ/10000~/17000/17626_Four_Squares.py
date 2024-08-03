from sys import stdin


n = int(stdin.readline())

lst = [0] * (n+1)
lst[1] = 1 # 1은 1의 제곱이니까

for i in range(2, n+1):
    cnt = 1 
    res = 4
    while (cnt ** 2) <= i:
        k = lst[i-(cnt**2)] # 문제의 답은 1~4로만 이루어져 있음. 모든 수의 제곱근을 i에서 빼고
        res = min(k, res) # 가장 작은 경우를 저장
        cnt += 1
    lst[i] = res + 1 # 이전의 숫자들에서 참조한거니까 +1 해주기

print(lst[n])
