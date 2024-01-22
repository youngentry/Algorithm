import sys

input = sys.stdin.readline

n = int(input())
hands = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

memo_dict = {}

for hand_num in hands:
    if not memo_dict.get(hand_num):
        memo_dict[hand_num] = 1
    else:
        memo_dict[hand_num] += 1


for target in targets:
    if not memo_dict.get(target):
        print(0, end=" ")
    else:
        print(memo_dict.get(target), end=" ")
