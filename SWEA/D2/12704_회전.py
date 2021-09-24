#[1]

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))

    front = 0  # 1번 자리를 바꾸면 lst의 인덱스 1번 자리가 맨 앞이라서 0번부터 시작


    j = 0
    while j < M:
        front = (front+1) % len(lst) 
        a = lst[front]
        j += 1

    print('#{} {}'.format(t,a))


######################################
#[2]
tc = int(input())

for t in range(1, tc+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))


    que = [0 for _ in range(2000)]

    front = 0
    rear = 0
    for i in range(N):
        que[rear] = lst[i]
        rear += 1

    j = 0
    while j < M:
        a = que[front] 
        front += 1
        que[rear] = a  # 계속 리스트에 값을 추가
        rear += 1
        j += 1

    print('#{} {}'.format(t, que[front]))


