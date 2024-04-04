import sys
input = sys.stdin.readline

# 0:상 1:우 2:하 3:좌
def roll(in_grid,dir, red, blue):
    global is_finished

    rolled_red = None
    rolled_blue = None
    copied_grid = [in_grid[row][:] for row in range(N)]

    goal_cnt = 0
    is_blue_first = False

    if dir == 0:
        # 위쪽에 있는 구슬부터 굴리기
        if red[0] < blue[0]:
            rx,ry = red
            while copied_grid[rx-1][ry] != "#" and copied_grid[rx-1][ry] !="B":
                if copied_grid[rx-1][ry] == "O":
                    goal_cnt += 1
                    copied_grid[rx][ry] = "."
                    break
                copied_grid[rx][ry], copied_grid[rx-1][ry] = copied_grid[rx-1][ry], copied_grid[rx][ry]
                rx = rx-1
            rolled_red = rx,ry # 새로운 위치로 갱신
            rx,ry = blue
            while copied_grid[rx-1][ry] != "#" and copied_grid[rx-1][ry] !="R":
                if copied_grid[rx - 1][ry] == "O":
                    if goal_cnt == 0:
                        is_blue_first = True
                    goal_cnt += 1
                    break
                copied_grid[rx][ry], copied_grid[rx-1][ry] = copied_grid[rx-1][ry], copied_grid[rx][ry]
                rx = rx-1
            rolled_blue = rx,ry
        else:
            rx,ry = blue
            while copied_grid[rx-1][ry] != "#" and copied_grid[rx-1][ry] !="R":
                if copied_grid[rx-1][ry] == "O":
                    is_blue_first = True
                    goal_cnt += 1
                    copied_grid[rx][ry] = "."
                    break
                copied_grid[rx][ry], copied_grid[rx-1][ry] = copied_grid[rx-1][ry], copied_grid[rx][ry]
                rx = rx-1
            rolled_blue = rx,ry # 새로운 위치로 갱신
            rx,ry = red
            while copied_grid[rx-1][ry] != "#" and copied_grid[rx-1][ry] !="B":
                if copied_grid[rx - 1][ry] == "O":
                    goal_cnt += 1
                    break
                copied_grid[rx][ry], copied_grid[rx-1][ry] = copied_grid[rx-1][ry], copied_grid[rx][ry]
                rx = rx-1
            rolled_red = rx,ry

    elif dir == 1:
        # 오른쪽에 있는 구슬부터 굴리기
        if red[1] > blue[1]:
            rx,ry = red
            while copied_grid[rx][ry+1] != "#" and copied_grid[rx][ry+1] !="B":
                if copied_grid[rx][ry+1] == "O":
                    goal_cnt += 1
                    copied_grid[rx][ry] = "."
                    break
                copied_grid[rx][ry], copied_grid[rx][ry+1] = copied_grid[rx][ry+1], copied_grid[rx][ry]
                ry = ry+1
            rolled_red = rx,ry # 새로운 위치로 갱신
            rx,ry = blue
            while copied_grid[rx][ry+1] != "#" and copied_grid[rx][ry+1] !="R":
                if copied_grid[rx][ry+1] == "O":
                    if goal_cnt == 0:
                        is_blue_first = True
                    goal_cnt += 1
                    break
                copied_grid[rx][ry], copied_grid[rx][ry+1] = copied_grid[rx][ry+1], copied_grid[rx][ry]
                ry = ry+1
            rolled_blue = rx,ry
        else:
            rx,ry = blue
            while copied_grid[rx][ry+1] != "#" and copied_grid[rx][ry+1] !="R":
                if copied_grid[rx][ry+1] == "O":
                    is_blue_first = True
                    goal_cnt += 1
                    copied_grid[rx][ry] = "."
                    break
                copied_grid[rx][ry], copied_grid[rx][ry+1] = copied_grid[rx][ry+1], copied_grid[rx][ry]
                ry = ry+1
            rolled_blue = rx,ry # 새로운 위치로 갱신
            rx,ry = red
            while copied_grid[rx][ry+1] != "#" and copied_grid[rx][ry+1] !="B":
                if copied_grid[rx][ry+1] == "O":
                    goal_cnt += 1
                    break
                copied_grid[rx][ry], copied_grid[rx][ry+1] = copied_grid[rx][ry+1], copied_grid[rx][ry]
                ry = ry+1
            rolled_red = rx,ry



    elif dir == 2:
        # 아래쪽에 있는 구슬부터 굴리기
        if red[0] > blue[0]:
            rx,ry = red
            while copied_grid[rx+1][ry] != "#" and copied_grid[rx+1][ry] !="B":
                if copied_grid[rx+1][ry] == "O":
                    goal_cnt += 1
                    copied_grid[rx][ry] = "."
                    break
                copied_grid[rx][ry], copied_grid[rx+1][ry] = copied_grid[rx+1][ry], copied_grid[rx][ry]
                rx = rx+1
            rolled_red = rx,ry # 새로운 위치로 갱신
            rx,ry = blue
            while copied_grid[rx+1][ry] != "#" and copied_grid[rx+1][ry] !="R":
                if copied_grid[rx + 1][ry] == "O":
                    if goal_cnt == 0:
                        is_blue_first = True
                    goal_cnt += 1
                    break
                copied_grid[rx][ry], copied_grid[rx+1][ry] = copied_grid[rx+1][ry], copied_grid[rx][ry]
                rx = rx+1
            rolled_blue = rx,ry
        else:
            rx,ry = blue
            while copied_grid[rx+1][ry] != "#" and copied_grid[rx+1][ry] !="R":
                if copied_grid[rx+1][ry] == "O":
                    is_blue_first = True
                    goal_cnt += 1
                    copied_grid[rx][ry] = "."
                    break
                copied_grid[rx][ry], copied_grid[rx+1][ry] = copied_grid[rx+1][ry], copied_grid[rx][ry]
                rx = rx+1
            rolled_blue = rx,ry # 새로운 위치로 갱신
            rx,ry = red
            while copied_grid[rx+1][ry] != "#" and copied_grid[rx+1][ry] !="B":
                if copied_grid[rx + 1][ry] == "O":
                    goal_cnt += 1
                    break
                copied_grid[rx][ry], copied_grid[rx+1][ry] = copied_grid[rx+1][ry], copied_grid[rx][ry]
                rx = rx+1
            rolled_red = rx,ry

    elif dir == 3:
        # 왼쪽에 있는 구슬부터 굴리기
        if red[1] < blue[1]:
            # print('redf')
            rx,ry = red
            while copied_grid[rx][ry-1] != "#" and copied_grid[rx][ry-1] !="B":
                if copied_grid[rx][ry-1] == "O":
                    goal_cnt += 1
                    copied_grid[rx][ry] = "."
                    break
                copied_grid[rx][ry], copied_grid[rx][ry-1] = copied_grid[rx][ry-1], copied_grid[rx][ry]
                ry = ry-1
            rolled_red = rx,ry # 새로운 위치로 갱신
            rx,ry = blue
            while copied_grid[rx][ry-1] != "#" and copied_grid[rx][ry-1] !="R":
                if copied_grid[rx][ry-1] == "O":
                    if goal_cnt == 0:
                        is_blue_first = True
                    goal_cnt += 1
                    break
                copied_grid[rx][ry], copied_grid[rx][ry-1] = copied_grid[rx][ry-1], copied_grid[rx][ry]
                ry = ry-1
            rolled_blue = rx,ry
        else:
            # print('bluef')
            rx,ry = blue
            while copied_grid[rx][ry-1] != "#" and copied_grid[rx][ry-1] !="R":
                if copied_grid[rx][ry-1] == "O":
                    is_blue_first = True
                    goal_cnt += 1
                    copied_grid[rx][ry] = "."
                    break
                copied_grid[rx][ry], copied_grid[rx][ry-1] = copied_grid[rx][ry-1], copied_grid[rx][ry]
                ry = ry-1
            rolled_blue = rx,ry # 새로운 위치로 갱신
            rx,ry = red
            while copied_grid[rx][ry-1] != "#" and copied_grid[rx][ry-1] !="B":
                if copied_grid[rx][ry-1] == "O":
                    goal_cnt += 1
                    break
                copied_grid[rx][ry], copied_grid[rx][ry-1] = copied_grid[rx][ry-1], copied_grid[rx][ry]
                ry = ry-1
            rolled_red = rx,ry

    if goal_cnt == 2:
        return copied_grid, rolled_red, rolled_blue, goal_cnt, is_blue_first
    if goal_cnt == 1 and not is_blue_first:
        # print(red,blue,rolled_red,rolled_blue,dir)
        is_finished = True
    return copied_grid, rolled_red, rolled_blue, goal_cnt, is_blue_first


def dfs(n, copied_grid, dir, red, blue, route):
    global is_finished

    if n==11:
        return

    if is_finished:
        return

    # 굴리기
    rolled_grid, rolled_red, rolled_blue, goal_cnt, is_blue_first = roll(copied_grid,dir, red, blue)

    if is_blue_first:
        return

    if goal_cnt == 2:
        return

    if is_finished:
        return

    for i in range(4):
        dfs(n+1, rolled_grid, i, rolled_red, rolled_blue, route+[dir])


N,M = map(int,input().split())
red = 0,0
blue = 0,0
grid = []
for i in range(N):
    line = list(input().strip())
    for j in range(M):
        if line[j] == "R":
            red = i,j
        elif line[j] == "B":
            blue = i,j

    grid.append(line)

copied = [grid[row][:] for row in range(N)]
# print(copied)

is_finished = False
# 0:상 1:우 2:하 3:좌
for i in range(4):
    dfs(1, copied, i, red[:], blue[:], [i])

if is_finished:
    print(1)
else:
    print(0)