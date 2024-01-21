import sys
input = sys.stdin.readline

# 서로 다른 네 종류의 치즈가 토핑
# 토핑의 이름이 Cheese로 끝나면 이 토핑이 치즈
N = int(input())
words = list(input().split())
cheese_dict = {}
for word in words:
    if word[-6:] == "Cheese":
        cheese_dict[word] = True

if len(cheese_dict)>=4:
    print('yummy')
else:
    print('sad')