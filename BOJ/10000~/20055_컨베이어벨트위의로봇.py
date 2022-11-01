from sys import stdin
from collections import deque
N, K = map(int, stdin.readline().split())
belt = deque(list(map(int, stdin.readline().split())))

robot = deque([0] * N)

res = 0

while True:
    # 문제에서 1번 단계
    b = belt.pop() # belt.rotate(1)
    belt.appendleft(b)
    r = robot.pop() # robot.rotate(1)
    robot.appendleft(r) 

    robot[-1] = 0  # 내릴 자리에 도착한 로봇은 0으로 처리

    # 2번 단계
    for i in range(N-2, -1, -1): # 가장 먼저 올라간 로봇부터 처리, 마지막 로봇은 내려야하니까 마지막 바로 전 로봇부터
        if robot[i] and not robot[i+1] and belt[i+1]: # 로봇이 있고 바로 앞자리에 로봇이 없고 내구도가 있는 경우
            belt[i+1] -= 1 # 내구도 빼주기
            robot[i], robot[i+1] = 0, 1

    robot[-1] = 0 # 내릴 자리에 도착할 경우 빼주기


    # 3번 단계
    if belt[0] and not robot[0]: # 첫번째 자리에 내구도가 있고 로봇이 없는 경우
        belt[0] -= 1
        robot[0] = 1 # 로봇 올려주기

    if belt.count(0) >= K: # 0이 K이상일 경우 멈추기
        res += 1
        break
    res += 1

print(res)