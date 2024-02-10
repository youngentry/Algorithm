import sys
input = sys.stdin.readline

# L미터의 롤케이크
# 1~L번 조각
# N명에게 나누어줌
# 1~N번 방청객

L = int(input())
N = int(input())
cake = [0]*(L+1)

expected = 0
expected_count = 0


for i in range(1,N+1):
    s,e = map(int,input().split())
    # cake[s:e+1] = [i]*(e-s+1)
    for j in range(s,e+1):
        if cake[j] == 0:
            cake[j] = i
    # print(e-s+1,i,"-",expected < e-s+1)
    if expected_count < e-s+1:
        expected_count = e-s+1
        expected = i
    # print(expected,"ex")

cnt = [0]*(N+1)
# print(cake)
print(expected)

for num in cake:
    cnt[num] += 1
cnt[0] = 0
# print(cnt)
# print(max(cnt))
print(cnt.index(max(cnt)))