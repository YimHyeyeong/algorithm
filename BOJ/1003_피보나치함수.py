def fibo(n):
    if n >= len(zero):  # 리스트 안의 값을 중복 사용하지 않기 위해서, len보다 작으면 그 안에서 찾으면 됨
        for i in range(len(zero), n+1): 
            zero.append(zero[i-1] + zero[i-2])  # 0를 사용한 횟수는 (i-1) + (i-2) 이다 
            one.append((one[i-1] + one[i-2]))




T = int(input())

for _ in range(T):
    N = int(input())
    zero = [1,0,1]   # 각 인덱스 별로 0을 사용한 횟수를 저장 ex) 0은 0을 한 번 사용 , 2도 한 번 사용
    one = [0,1,1]  # 각 인덱스 별로 1을 사용한 횟수를 저장  ex) 0은 1을 사용하지 않음. 1은 1번 사용
    fibo(N)
    print('{} {}'.format(zero[N],one[N]))

