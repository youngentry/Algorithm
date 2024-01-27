import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))
number_set = set(numbers)
sorted_numbers = (sorted(number_set))

_dict = {}
for i,num in enumerate(sorted_numbers):
    _dict[num] = i

for i in range(n):
    numbers[i] = _dict[numbers[i]]

print(*numbers)