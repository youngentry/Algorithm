import sys
input = sys.stdin.readline

def rotate(base,longer):
    rotated = [[0]*longer for _ in range(longer)]
    for i in range(longer):
        for j in range(longer):
            rotated[j][longer-1-i] = base[i][j]
    return rotated


N,M,K = map(int,input().split()) 
stickers = []
for _ in range(K):
    R,C = map(int,input().split())
    longer = max(R,C)

    rotate0 = [[0]*longer for _ in range(longer)]
    for i in range(R):
        row = list(map(int,input().split()))
        for j in range(C):
            rotate0[i][j] = row[j]
    rotate90 = rotate(rotate0,longer)
    rotate180 = rotate(rotate90,longer)
    rotate270 = rotate(rotate180,longer)

    rotations = [None]*4
    if R<C: # 가로가 더 길면
        rotations[0] = rotate0[0:R]
        rotations[1] = [row[C-R:] for row in rotate90]
        rotations[2] = rotate180[C-R:]
        rotations[3] = [row[:R] for row in rotate270]
    else: # 세로가 더 길면
        rotations[0] = [row[0:C] for row in rotate0]
        rotations[1] = rotate90[0:C]
        rotations[2] = [row[R-C:] for row in rotate180]
        rotations[3] = rotate270[R-C:]

    stickers.append(rotations)


# 못 붙이겠다면 90도 회전 시킨 뒤 시도함
grid = [[0]*M for _ in range(N)]
for i in range(K): # 스티커 K개 붙이기
    cur_sticker = stickers[i] # stickers[i] 에는 각 스티커의 0,90,180,270 이 들어 있음

    for j in range(4):
        rotated_sticker = cur_sticker[j]
        row,col = len(rotated_sticker), len(rotated_sticker[0])
        is_used = False
        for q in range(N-row+1): # (가장 위쪽 최우선)으로 붙이기를 이동하면서 시도함
            if is_used: break 
            for w in range(M-col+1): # => 다음으로 왼쪽 우선
                if q+row > N or w+col >M: break
                if is_used: break
                is_ok = True # 가능성 판정
                for e in range(row):
                    for r in range(col):
                        if grid[q+e][w+r] == 1 and rotated_sticker[e][r] == 1:
                            is_ok = False
                if is_ok: # 실제로 붙이기
                    for e in range(row):
                        for r in range(col):
                            if rotated_sticker[e][r]:
                                grid[q+e][w+r] = 1
                                is_used = True
        if is_used: break

ans = 0
for i in range(N):
    for j in range(M):
        if grid[i][j]:
            ans += 1
print(ans)