import sys
import math
from collections import deque
input = sys.stdin.readline

N = int(input())

first_word = input().strip()
result = 0

for _ in range(N-1):
    compare_word = input().strip()
    base_checked = [0] * len(first_word)
    compare_checked = [0] * len(compare_word)
    count = 0

    for i in range(len(first_word)):
        base_alphabet = first_word[i]
        for k in range(len(compare_word)):
            compare_alphabet = compare_word[k]

            if base_alphabet == compare_alphabet and not compare_checked[k] and not base_checked[i]:
                count += 1
                base_checked[i] = 1
                compare_checked[k] = 1

    if len(compare_word) == len(first_word):
        # print('--------------------   same')
        if count >= len(first_word) -1:
            result += 1
    elif len(compare_word) +1 == len(first_word):
#         print('-----------------      +1')
        if count == len(compare_word):
            result += 1
    elif len(compare_word) -1 == len(first_word):
#         print('------------------     -1')
        if count == len(first_word):
            result += 1
    # print(compare_word, count)

print(result)
