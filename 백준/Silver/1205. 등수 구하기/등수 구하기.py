import sys
input = sys.stdin.readline


N, score, P = map(int,input().split())


score_list = []

if N != 0:
    score_list = list(map(int,input().split()))

score_list.append(score)

score_list.sort(reverse=True)

if score_list[-1] == score and len(score_list) > P:
    print(-1)
else:
    score_list = score_list[0:P]

    rank = 1
    for num in score_list:
        if num == score:
            print(rank)
            break
        else:
            rank += 1
