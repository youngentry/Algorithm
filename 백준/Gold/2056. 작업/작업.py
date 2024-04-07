import sys
input = sys.stdin.readline
from collections import deque

# start_time = time.time()
# ======================================

N = int(input())
in_degree = [0]*(N+1) # 1~N 번 진입 차수
graph = [[] for _ in range(N+1)] # 진입 차수가 0이 되었을 때 수행할 작업
times = [0]*(N+1) # 1~N 번 작업 수행에 필요한 시간
for i in range(1,N+1):
    time, cnt, *need_works = map(int,input().split())
    times[i] = time
    if cnt != 0:
        for need_work in need_works:
            in_degree[i] += 1
            graph[need_work].append(i)

dp = [0]*(N+1) # N번 작업을 수행하기 위해 필요한 가장 큰 시간 기록
queue = deque()
for i in range(1,N+1):
    if in_degree[i] == 0:
        queue.append(i) # 진입 차수가 0인 작업 번호 추가
        dp[i] = times[i] # N번 작업 수행에 필요한 기본 시간

result = [] # 작업 진행 순서
while queue:
    cur = queue.popleft() # 진입 차수가 0인 작업 번호
    result.append(cur)
    for next_node in graph[cur]:
        in_degree[next_node] -= 1 # 작업 수행 => 진입 차수 -1
        # 다음 작업을 수행하기 위해 필요한 가장 긴 작업시간을 저장
        dp[next_node] = max(dp[next_node], dp[cur]+times[next_node]) 
        if in_degree[next_node] == 0: # 진입차수가 0이 되었다면 모든 선행 작업을 수행한 것
            queue.append(next_node) # 새롭게 진입차수가 0이 된 작업을을 큐에 추가
print(max(dp))

# if len(result) == len(graph): # 그래프에 순환이 없는지 확인
#     print(result)
# else:
#     print("그래프에 순환 구조가 있어 위상 정렬이 불가능한 경우")

# ======================================
# print(time.time() - start_time)
