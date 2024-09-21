import sys
input = sys.stdin.readline

N = int(input())
slimes = list(map(int,input().split()))

sorted_slimes = sorted(slimes,reverse=True)

size = 0
score = 0
for i in range(0,N-1):
    score += sorted_slimes[i+1]*sorted_slimes[i]
    sorted_slimes[i+1] += sorted_slimes[i]

print(score)