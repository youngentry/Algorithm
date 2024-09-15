
N,M = map(int,input().split())
#  N개의 달걀이 있고, 그의 잠재적인 고객은 총 M명
# 각각의 i번째 고객은 각자 달걀 하나를 Pi 가격 이하로 살 수 있다
# 한 고객에게 두 개 이상의 달걀은 팔지 않기
# 수익은 최대로 올리고 싶기에 얼마로 팔지 고민
# arr에 숫자들을 카운트.

val_num_counts = {}
for i in range(M):
    num = int(input())
    if num in val_num_counts:
        val_num_counts[num] += 1
    else:
        val_num_counts[num] = 1

arr = []
for key in val_num_counts:
    arr.append((key, val_num_counts[key]))
arr.sort(reverse=True)
# print(arr)
people_count = M
max_revenue = 0
per_revenue = 0
while arr:
    val,num = arr.pop()
    while num and people_count > N:
        num -= 1
        people_count -= 1
    if not num:
        continue
    if max_revenue < val * people_count:
        max_revenue = val * people_count
        per_revenue = val
    people_count -= num

print(per_revenue, max_revenue)