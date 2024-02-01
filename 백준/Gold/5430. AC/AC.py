import sys
from collections import deque
from copy import deepcopy
from itertools import permutations, combinations
from string import ascii_lowercase

t = int(input())
for tc in range(t):
    p = input().strip()
    n = int(input())
    numbers = input().strip()[1:-1].split(",")
    # print(numbers)

    left, right = 0, n
    is_bad = False
    is_flipped = False
    for alpha in p:
        # print(left, right,"?")
        if alpha == "R":
            is_flipped = not is_flipped
        if alpha == "D":
            if left==right:
                is_bad = True
                break
            if is_flipped:
                right -= 1
            else:
                left += 1
    # print(is_flipped,left,right)
    if is_bad:
        print('error')
    else:
        if is_flipped:
            print(str(list(map(int,numbers[left:right][::-1]))).replace(" ",""))

        else:
            print(str(list(map(int,numbers[left:right]))).replace(" ",""))

