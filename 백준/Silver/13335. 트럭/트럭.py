import sys
from collections import deque

input = sys.stdin.readline

# n개의 트럭이 건넘
# 트럭 순서 유지(큐)
# 트럭 무게 다름
# W대의 트럭만 올라갈 수 있음
# 다리 길이는 w 단위길이
# 각 트럭은 하나의 단위시간에 하나의 단위길이만 기동
# 트럭무게합은 다리 최대하중 L보다 작거나 같은
# 다리에 완전히 올라간 트럭 무게만 계산

# ex)
# 다리길이 W2
# 다리하중 L10
# 트럭무게[7,4,5,6]
# 최단시간은 8

n,w,l = map(int,input().split())
truck_count,length,load = n,w,l
trucks = deque((map(int,input().split())))
bridge = deque([])
goal = 0
total_time = 0
while goal < n:
    if len(bridge) and bridge[0][0] == w:
        # 트럭이 내려가면 => 다리하중+wei, 다리길이여유+1
        off_truck = bridge.popleft()
        load += off_truck[1]
        length += 1
        goal += 1

    # 현재다리하중보다 적음 and 현재다리길이여유 있음 ? 트럭 올라가기
    if  len(trucks) and load >= trucks[0] and length > 0:
        # 트럭이 올라가면 => 다리하중+wei, 다리길이여유-1
        on_truck = trucks.popleft()
        load -= on_truck
        length -= 1
        bridge.append([0,on_truck])

    # 다리위의 모든 트럭 시간 +1
    for i in range(len(bridge)):
        bridge[i][0] += 1
    total_time += 1

print(total_time)