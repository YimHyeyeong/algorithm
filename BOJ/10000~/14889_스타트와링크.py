from sys import stdin
from itertools import combinations

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

members = [i for i in range(N)]
team_lst = []

for j in list(combinations(members, N//2)): # 조합이 가능한 팀목록 만들기
    team_lst.append(j)

res = 21e8

for k in range(len(team_lst)//2):
    start_team = team_lst[k] # start 팀
    start = 0 # start팀 능력치
    for q in range(len(start_team)):
        for m in start_team:
            start += arr[start_team[q]][m]

    link_team = team_lst[-k-1]  # start팀을 제외한 나머지 멤버의 조합
    link = 0 # link팀의 능력치
    for g in range(len(link_team)):
        for s in link_team: # 본인의 능력치는 0이니까 괜찮음
            link += arr[link_team[g]][s]

    res = min(res, abs(start-link)) 

print(res)
