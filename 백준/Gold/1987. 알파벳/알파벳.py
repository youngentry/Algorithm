import sys
input = sys.stdin.readline

def dfs(x,y,move):
    global max_move
    max_move = max(max_move,move) # 최대 카운트 저장

    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<R and 0<=ny<C:
            alp_ord = ord(board[nx][ny])
            if alphabet_base[alp_ord] == 0:
                # 재귀적으로 백트래킹
                alphabet_base[alp_ord] = 1
                dfs(nx,ny,move+1)
                alphabet_base[alp_ord] = 0


# 입력값 받기
R,C = map(int,input().split())
board = []
for row in range(R):
    board.append(list(input().strip()))

alphabet_base = [0]*128 # 알파벳 존재 여부
max_move = 0
alphabet_base[ord(board[0][0])] = 1 # 시작지점 방문처리

directions = [[-1,0],[0,1],[1,0],[0,-1]]
result = dfs(0,0,1)

print(max_move)