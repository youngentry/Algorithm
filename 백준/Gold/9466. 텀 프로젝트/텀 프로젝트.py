import sys
sys.setrecursionlimit(100000)  # 재귀 깊이 제한 설정
from collections import deque
import heapq
import time
input = sys.stdin.readline  # 입력 속도를 높이기 위해 sys.stdin.readline 사용

# st = time.time()
# ======================================

def dfs(i):
    global route  
    global ans 

    route.append(i)  # 경로에 현재 노드 추가
    v[i] = 1  # 방문 표시

    if v[numbers[i]] == 0:  # 아직 다음 노드가 방문하지 않은 노드라면
        dfs(numbers[i])  # 다음 노드 방문
    else:  # 이미 방문한 노드라면
        if numbers[i] in route:  # 사이클의 시작점을 찾아서 존재한다면
            ans += len(route[route.index(numbers[i]):])  # 사이클 부분의 길이를 더함

T = int(input())  
for tc in range(T):
    N = int(input()) 
    numbers = [0]+list(map(int,input().split())) 
    v = [1]+[0]*N 
    ans = 0  
    for i in range(1,N+1):
        if v[i] == 0:  # 방문하지 않은 노드라면
            route = [] # 싸이클 경로
            dfs(i)  

    print(N-ans)  # 결과 출력

# ======================================
# print(time.time() - st)
