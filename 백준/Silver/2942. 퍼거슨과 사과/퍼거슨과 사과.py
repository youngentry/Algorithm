import sys
from _collections import deque

R, G = map(int,input().split())
#
# 모든 선수에게 같은 개수 지급
#
# 사과가 남으면안됨
#
# R과 G각각의 약수를 구함
R_mods = set()
G_mods = set()

for i in range(1, int(R**0.5) + 1):
    if R % i == 0:
        R_mods.add(i)
        R_mods.add(R//i)
for i in range(1, int(G**0.5) + 1):
    if G % i == 0:
        G_mods.add(i)
        G_mods.add(G//i)


found_nums = []
while R_mods:
    check_num = R_mods.pop()
    if check_num in G_mods:
        found_nums.append(check_num)

for num in found_nums:
    print(num, R//num, G//num)