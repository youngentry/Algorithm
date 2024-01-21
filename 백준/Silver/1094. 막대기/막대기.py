import sys
input = sys.stdin.readline

total_cm = int(input().strip())
count = 0

for i in range(6,-1,-1):
    if total_cm >= 2**i:
        total_cm = total_cm % 2**i
        count+=1

print(count)