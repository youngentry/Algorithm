import sys
import math
input = sys.stdin.readline

counts = {}

N,M = map(int,input().split())

for i in range(N):
    word = input().strip()

    if len(word) >= M:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

items = list(counts.items())

result = sorted(items,key=lambda x:(-x[1],-len(x[0]),x))
for word in result:
    print(word[0])