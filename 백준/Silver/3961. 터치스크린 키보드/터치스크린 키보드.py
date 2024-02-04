import sys

input = sys.stdin.readline

t = int(input())

# 각 알파벳에 대해 해시를 생성
# 비교 문자별로 해시값의 합산 정보를 추가
# 오름차순으로 정렬하여 출력

keyboard = []
top = list("qwertyuiop")
mid = list("asdfghjkl ")
bot = list("zxcvbnm   ")
keyboard.append(top)
keyboard.append(mid)
keyboard.append(bot)
# print(*keyboard,sep='\n')

map = {}
for i in range(3):
    for j in range(10):
        map[keyboard[i][j]] = {}

# print(map)
for p in range(3):
    for q in range(10):
        cur = keyboard[p][q]
        for j in range(3):
            for k in range(10):
                compare = keyboard[j][k]
                map[cur][compare] = abs(p-j) + abs(q-k)
# print(map)

for tc in range(t):
    word,l = input().split()
    l = int(l)

    compares = []
    for _ in range(l):
        compares.append(input().strip())

    # print(word)
    # print(compares)
    results = []
    for compare in compares:
        count = 0
        # print(compare,"?")
        for i in range(len(compare)):
            count += map[word[i]][compare[i]]
        results.append([compare,count])
    sorted_result = sorted(results, key=lambda x:(x[1], x[0]))
    for item in sorted_result:
        print(f'{item[0]} {item[1]}')