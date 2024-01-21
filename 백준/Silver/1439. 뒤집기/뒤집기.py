import sys

input = sys.stdin.readline

line=input().strip()
numbers = (line.split("1"))
numbers0 = (line.split("0"))

count = 0
count0 = 0
for number in numbers:
    if "0" in number:
        count+=1

for number in numbers0:
    if "1" in number:
        count0+=1

print(min(count,count0))
