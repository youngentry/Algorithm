import sys

input = sys.stdin.readline

N, K = map(int,input().split())

nations = []

for i in range(N):
    nations.append(list(map(int,input().split())))

nations.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)

is_done = False

rank = 1
skip_count = 1
for i in range(N-1):
    # print(rank,skip_count)
    # 금메달 수가 더 많은 경우
    if nations[i][1] > nations[i+1][1]:
        if nations[i][0] == K:
            print(rank)
            is_done = True
            break
        else:
            rank += skip_count
            skip_count = 1
            continue

    # 금메달 수는 같은데
    # 은메달 수가 더 많은 경우
    if nations[i][2] > nations[i + 1][2]:
        if nations[i][0] == K:
            print(rank)
            is_done = True
            break
        else:
            rank += skip_count
            skip_count += 1
            continue

    # 금, 은메달 수가 같고
    # 동메달 수가 더 많은 경우
    if nations[i][3] > nations[i + 1][3]:
        if nations[i][0] == K:
            print(rank)
            is_done = True
            break
        else:
            rank += skip_count
            skip_count += 1
            continue

    skip_count += 1

if not is_done:
    print(rank)