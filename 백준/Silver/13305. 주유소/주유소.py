import sys

input = sys.stdin.readline

# 다음 도시가 낮은 가격이면 
# 남은기름 - 간선 만큼만 구매

# 더 낮은 가격의 도시를 발견할 때까지
# 남은기름 - 간선의 합 만큼 구매
# 도시의 수만큼 i 건너뛰기

n = int(input())
edges = list(map(int,input().split()))
cities = list(map(int,input().split()))

current_city = cities[0]
edge_sum = 0
remain_oil = 0
price = 0
for i in range(1,n):
  edge_sum += edges[i-1]
  # 낮은 가격 발견
  if cities[i] < current_city:
    price += (remain_oil+edge_sum)*current_city
    edge_sum = 0
    current_city = cities[i]
  # else:
  #   edge_sum += edges[i-1]

print(price + edge_sum * current_city)