import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
# print(numbers)

xy = set()
for i in range(N):
    for j in range(N):
        xy.add(numbers[i]+numbers[j])

def find_xyz():
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if numbers[i]-numbers[j] in xy:
                print(numbers[i])
                return

find_xyz()