#[1] 트럭과 무게리스트 모두 정렬했을 때
tc = int(input())

for t in range(1,tc+1):
    N,M = map(int,input().split( ))
    weight = list(map(int,input().split()))
    truck = list(map(int,input().split()))

    weight.sort()  # 정렬 후
    truck.sort()
    res = 0
    while truck:
        T = truck.pop() # 가장 뒤의 값 = 가장 큰 값을 뽑고
        while weight:
            W = weight.pop()  # 가장 무거운 컨테이너도 뽑아내서
            if T >= W:  # 비교
                res += W
                break
    print('#{} {}'.format(t,res))


###################
#[2] 트럭만 정렬했을 때
T = int(input())

for tc in range(1, T + 1) :
    N,M = map(int ,input().split())
    load = list(map(int , input().split()))
    truck = list(map(int, input().split()))

    # 트럭 내림차순으로 정렬하기
    truck.sort(reverse = True) 
    used = [0] * N  # 사용한 컨테이너를 표시
    ans = 0
    for t in range(len(truck)) :
        # 제일 큰거 찾기
        idx = -1   # 가장 크고 트럭보다 큰 값의 인덱스 저장
        max_load = -int(21e8)
        for i in range(len(load)):
            if used[i] == 1 : continue  # 이미 가져간? 컨테이너는 건너뛰기
            if max_load < load[i] and truck[t] >= load[i] : 
                idx = i
                max_load = load[i]

        # truck[t] 에 실을까?
        if idx != -1:  # -1인건 실을 수 있는 것이 없다.
            used[idx] = 1 # 사용한 컨테이너 저장
            ans += load[idx]

    print("#{} {}".format(tc, ans))
