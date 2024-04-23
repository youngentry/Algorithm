import sys
from collections import deque

def rotate(color,dir_i):
    dx,dy = dirs[dir_i]
    cx,cy = color
    for i in range(1,13):
        cx,cy = cx+dx, cy+dy
        if grid[cx][cy] == "#":
            return ([cx-dx,cy-dy], i, False)
            break
        elif grid[cx][cy] == "O":
            return ([cx,cy], i, True)
            break


N,M = map(int,input().split())
grid = [list(input().strip()) for _ in range(N)]

red = None
blue = None

for i in range(N):
    for j in range(M):
        if grid[i][j] == "B":
            blue = [i,j]
        elif grid[i][j] == "R":
            red = [i,j]

moves = deque([(red,blue,1)])
move_set = set()
# move_set.add(str(red)+str(blue))
dirs = ((-1,0),(0,1),(1,0),(0,-1))
cnt = 0
ans = 0
is_finish = False
while moves and is_finish == False:
    is_same_pos = False

    cred,cblue,rotate_cnt = moves.popleft()
    if rotate_cnt == 11:
        continue

    # print(red,blue, '시작-------------',"rotate_cnt",rotate_cnt)
    for i in range(4):
        red, r_move_cnt, r_is_goal = rotate(cred[:],i)
        blue, b_move_cnt, b_is_goal = rotate(cblue[:],i)

        # print(red,blue,"??",r_is_goal,b_is_goal,rotate_cnt, i)
        if b_is_goal: # b가 골이라면 종료
            # print("B 골")
            continue
        if r_is_goal: # r가 골이라면 종료
            ans = rotate_cnt
            is_finish = True
            # print("R 골")
            break
        if red == blue:
            if r_move_cnt > b_move_cnt: # red 가 더 많이 움직였다면
                red[0] -= dirs[i][0]
                red[1] -= dirs[i][1]
            else: # blue 가 더 많이 움직였다면
                blue[0] -= dirs[i][0]
                blue[1] -= dirs[i][1]
        # print(red,blue,'red,bluered,bluered,blue')

        # 중복된 좌표라면 넘기기
        if (str(red)+str(blue)) in move_set:
            # print(str(red) + str(blue), move_set, "중복")
            continue

        move_set.add(str(red)+str(blue))
        moves.append((red[:],blue[:],rotate_cnt+1))

if not is_finish:
    print(-1)
else:
    print(ans)