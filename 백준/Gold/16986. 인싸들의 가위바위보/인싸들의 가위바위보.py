import sys
input = sys.stdin.readline

def dfs(round, wins,cnt,rival,results,counts):
    global K
    global N
    global is_win

    # print(round,results)

    if is_win: return               # 승리한 경우가 존재하면 더 볼 필요 없음

    if results[0] >= K:             # 지우 승리
        is_win = True
        return
    elif results[1] >= K: return    # 경희 승리
    elif results[2] >= K: return    # 민호 승리


    if 0 not in rival:              # 지우가 포함되어 있지 않은 경기
        p1, p2 = rival
        show1, show2 = shows[p1][counts[p1]], shows[p2][counts[p2]]
        if grid[show1-1][show2-1] == 1:             # 무승부인 경우
            if p1<p2:
                winner = p2
            else:
                winner = p1
        elif grid[show1-1][show2-1] == 2:           # p1 승자인 경우
            winner = p1
        elif grid[show1-1][show2-1] == 0:           # p2 승자인 경우
            winner = p2

        results[winner] += 1
        counts[p1]+=1
        counts[p2]+=1
        dfs(round+1,wins,cnt,(winner,0),results,counts)
        counts[p1]-=1
        counts[p2]-=1
        results[winner] -= 1

    else:                                           # 지우가 참가한다면
        if cnt == N:                                # 다 내버렸다면
            return

        for i in range(1,N+1):
            if v[i] == 1:                           # 모든 손동작 다르게 내기
                continue

            p1, p2 = rival
            show1, show2 = None, None
            if p1 == 0:
                show1 = i
                show2 = shows[p2][counts[p2]]
            elif p2 == 0:
                show1 = shows[p1][counts[p1]]
                show2 = i

            # p3 결정하기
            p3 = None
            if p1 == 0:
                if p2 == 1: p3 = 2
                elif p2 == 2: p3 = 1
            elif p1 == 1:
                if p2 == 0: p3 = 2
                elif p2 == 2: p3 = 0
            elif p1 == 2:
                if p2 == 0: p3 = 1
                elif p2 == 1: p3 = 0

            if grid[show1-1][show2-1] == 1:         # 무승부인 경우
                if p1<p2:
                    winner = p2
                else:
                    winner = p1
            elif grid[show1-1][show2-1] == 2:       # p1 승자인 경우
                winner = p1
            elif grid[show1-1][show2-1] == 0:       # p2 승자인 경우
                winner = p2

            v[i] = 1
            results[winner] += 1
            counts[p1] += 1
            counts[p2] += 1
            if winner == 0:                         # 지우 승인 경우
                dfs(round+1,wins+1,cnt+1,(winner,p3),results,counts)
            else:                                   # 지우 패인 경우
                dfs(round+1,wins,cnt+1,(winner,p3),results,counts)
            counts[p1] -= 1
            counts[p2] -= 1
            results[winner] -= 1
            v[i] = 0


N,K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
kyung = list(map(int,input().split()))
mino = list(map(int,input().split()))
shows = {0:False,1:kyung,2:mino}

v = [0]+[0]*N
path = []
is_win = False
dfs(0,0,0,(0,1),[0,0,0],[0,0,0])

if is_win:
    print(1)
else:
    print(0)
