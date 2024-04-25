import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 모든 숫자의 진입차수를 -1로 초기화
# 진입 차수를 먼저 풀면 좋은 문제 만큼 갱신
# -1이 아니면서, 가장 먼저 풀어야 하는 문제들을 heap에 push
# heap을 순서대로 출력하고
# 나머지 -1 숫자들에 대해서 출력하면 됨

N, M = map(int,input().split())

in_degrees = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
    in_degrees[e] += 1

# 0인 진입차수를 heap에 추가
pq = []
for i in range(1,N+1):
    if in_degrees[i] == 0:
        heappush(pq, i)

while pq:
    problem = heappop(pq)
    print(problem, end=" ")
    # num_set.remove(problem)
    for next_problem in graph[problem]:
        in_degrees[next_problem] -= 1
        if in_degrees[next_problem] == 0:
            heappush(pq, next_problem)
