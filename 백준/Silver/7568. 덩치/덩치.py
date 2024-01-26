import sys

input = sys.stdin.readline

n = int(input().strip()) # str.strip()으로 "\n" 과 같은 탈출 문자 제거
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

# 자신보다 덩치가 큰 사람이 몇 명인지 확인
for cur in lst:
    count = 1
    for j in range(n):
        if cur[0]<lst[j][0] and cur[1]<lst[j][1]:
            count += 1

    print(count, end=" ")