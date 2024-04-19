import sys
input = sys.stdin.readline

R,C,M = map(int,input().split())
R -= 1
C -= 1
sharks = []
for i in range(M):
    r, c, s, d, z = list(map(int,input().split()))
    sharks.append([r-1, c-1, s, d, z])

# 1:위 2:아래 3:오른 4:왼
dirs = ((0,0),(-1,0),(1,0),(0,1),(0,-1))
stand_idx = -1
ans = 0
sharks.sort(key=lambda x: (x[0], x[1], -x[4]))

# 끝점에 도달하면 종료
while stand_idx < C:
    # 1. 오른쪽으로 한 칸 이동
    stand_idx += 1

    # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
    for i in range(len(sharks)):
        # 같은 열이라면 확인
        if sharks[i][1] == stand_idx:
            popped = sharks.pop(i)
            ans += popped[4]
            break
    # 3. 상어 이동
    for i in range(len(sharks)):
        r,c,s,d,z = sharks[i]
        if d==1 or d==2: # 1상
            nr,nc = r+dirs[d][0]*s ,c+dirs[d][1]*s
            nr = nr % (2*R)
            if nr > R:
                sharks[i][0] = 2*R - nr
                sharks[i][3] = 2 if d==1 else 1
            else:
                sharks[i][0] = nr
        elif d==3 or d==4: # 3오
            nr,nc = r+dirs[d][0]*s ,c+dirs[d][1]*s
            nc = nc % (2*C)
            if nc > C:
                sharks[i][1] = 2*C - nc
                sharks[i][3] = 4 if d==3 else 3
            else:
                sharks[i][1] = nc

    # 4. 정렬하고 합치기
    sharks.sort(key=lambda x:(x[0],x[1],-x[4]))
    idx = 1
    while len(sharks) > 1 and idx < len(sharks):
        if sharks[idx-1][0] == sharks[idx][0] and sharks[idx-1][1] == sharks[idx][1]:
            sharks.pop(idx)
        else:
            idx += 1
print(ans)
