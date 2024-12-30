import sys
import math
input = sys.stdin.readline

N = int(input())
needs = list(map(int,input().split()))
total = int(input())

needs_sum = sum(needs)

result = 0

def is_possible(cost):
    global result

    # print('is_possible=>','cost',cost)
    acc = 0
    for need in needs:
        if cost >= need:
            acc += need
        else:
            acc += cost

    # print('is_possible=>''acc',acc,'total',total)

    if acc > total:
        return False
    else:
        return True


def binary_search(high):
    global result

    # print('high', high,'result',result)
    low = 0
    high = high

    while low <= high:
        mid = (low + high) // 2
        # print('mid',mid)

        if is_possible(mid):
            low = mid + 1
            result = mid
        else:
            high = mid - 1


if needs_sum > total:
    # print('dd')
    binary_search(total)
    print(result)
else:
    print(max(needs))