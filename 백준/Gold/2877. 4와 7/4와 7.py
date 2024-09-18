import math
import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
binary_num_from_second = format(K+1, 'b')[1:]

print(binary_num_from_second.replace('0', '4').replace('1', '7'))