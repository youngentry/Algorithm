import sys

input = sys.stdin.readline

# n:정수 개수, s:target
n, s = map(int,input().split())
numbers = list(map(int,input().split()))

combs = []

def get_comb(idx, size, part):
    # size에 도달하면 종료
    if idx == size+1:
        combs.append(part)
        return
    
    # 조합 생성
    for i in range(idx, n):
        part.append(numbers[i])
        get_comb(i+1, size, part[:])
        part.pop()

# 모든 길이에 대해 조합 생성
for i in range(n):
    get_comb(0, i, [])

# 조합의 합이 s인 경우 count+1
count = 0
for comb in combs:
    if sum(comb) == s:
        count+=1

print(count)