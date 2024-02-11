import sys
input = sys.stdin.readline

# 각 탑의 꼭대기에 레이저 송신기
# 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다. 

# stack을 이용해서
# top보다 큰 레이저를 만날 때까지 stack에 push를 반복
# top보다 큰 레이저를 만나면 stack에서 작은 수들을 계속 pop
# stack에 남아 있는 기둥은 모두 0으로

n = int(input())

towers = list(map(int,input().split()))
stack = []
memo = [0]*n
for i in range(n-1,0,-1):
    stack.append(i)

    # top보다 큰거 만났다
    while stack and towers[i-1] >= towers[stack[-1]]:
        top = stack.pop()
        memo[top] = i
    
print(*memo)