import sys

input = sys.stdin.readline

n = int(input())
tables = []
for i in range(n):
    tables.append(list(map(int,input().split())))

selected = [0]*n
result = 0

def comb(idx):
    global result

    for i in range(idx, n):
        time = tables[i][0]
        # 방문했으면 넘기기
        if selected[i]:
            continue

        # 이용 가능한 스케줄이면 추가
        if i + time <= n:
            selected[i] = 1
            comb(i + time)
            selected[i] = 0
    
    temp = 0
    for i in range(n):
        if selected[i]:
            temp += tables[i][1]
    result = max(result,temp)

comb(0)
print(result)