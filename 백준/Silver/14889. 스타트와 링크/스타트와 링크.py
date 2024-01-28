import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))


numbers = [i+1 for i in range(n)]
combs = list(combinations(numbers,n//2))
starts = (combs[:len(combs)//2])
links = (combs[len(combs)//2:][::-1])

min_score = float('inf')
for i in range(len(starts)):
    start_comb = list(combinations(starts[i],2))
    link_comb = list(combinations(links[i],2))
    # print(start_comb,link_comb)
    
    start_score = 0
    link_score = 0
    for x,y in start_comb:
        start_score += grid[x-1][y-1]
        start_score += grid[y-1][x-1]
    for x,y in link_comb:
        link_score += grid[x-1][y-1]
        link_score += grid[y-1][x-1]

    difference =  abs(start_score-link_score)
    min_score = min(min_score, difference)
    # print(start_score,link_score)

print(min_score)