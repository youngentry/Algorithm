import sys

input = sys.stdin.readline

n = int(input())

count = 0
num = 0
# "666"을 포함한 숫자를 하나씩 검사
while count < n:
    num += 1
    if "666" in str(num):
        count+=1

print(num)