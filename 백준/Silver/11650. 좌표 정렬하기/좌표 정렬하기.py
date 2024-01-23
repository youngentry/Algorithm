import sys

input = sys.stdin.readline

n = int(input())

coords = []
for _ in range(n):
    coords.append(list(map(int,input().split())))

sorted_coords = sorted(coords, key=lambda x: (x[0],x[1]))

for sorted_coord in sorted_coords:
    print(" ".join(map(str,sorted_coord)))