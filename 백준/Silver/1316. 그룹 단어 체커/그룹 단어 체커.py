import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

count = 0
for _ in range(T):
    word = input().strip()
    is_ok = True
    check_dict = {}

    for i in range(len(word)):
        # 연속이 아니고, 이미 존재하면 False하고 종료
        if i>0 and (word[i-1]!=word[i]) and (check_dict.get(word[i]) != None):
            is_ok = False
            break

        # 존재하지 않으면 기록하고
        if not check_dict.get(word[i]):
            check_dict[word[i]] = 1

    if is_ok:
        count +=1

    is_ok = True

print(count)