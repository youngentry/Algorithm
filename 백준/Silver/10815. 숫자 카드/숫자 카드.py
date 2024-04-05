import sys
input = sys.stdin.readline




N = int(input())
cards = list(map(int,input().split()))
card_set = set(cards)
M = int(input())
numbers = list(map(int,input().split()))
v = [0]*M
cnt = 0
for i in range(M):
    if numbers[i] in card_set:
        v[i] = 1
print(" ".join(map(str,v)))