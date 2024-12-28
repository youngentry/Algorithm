import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    runners = list(map(int,input().split()))

    teams = []

    for i in range(N):
        while runners[i] >= len(teams):
            teams.append(0)

        teams[runners[i]] += 1

    available_team_nums = set()

    for i in range(len(teams)):
        if teams[i] == 6:
            available_team_nums.add(i)

    race_teams = [[] for _ in range(len(teams))]
    score = 1
    for i in range(N):
        if runners[i] in available_team_nums:
            race_teams[runners[i]].append(score)
            score += 1

    result = []
    for idx,team_scores in enumerate(race_teams):
        if len(team_scores) > 1:
            result.append((idx,sum(team_scores[0:4]),team_scores[4]))

    result.sort(key=lambda x:(x[1],x[2]))
    print(result[0][0])