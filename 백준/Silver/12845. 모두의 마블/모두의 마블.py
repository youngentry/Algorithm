import sys
input = sys.stdin.readline

# 카드 A에 카드 B를 붙일 수 있음
# 1. 인접함
# 2. 카드 A 레벨 변화 없음
# 합성 : 두 카드 레벨의 합만큼 골드 받음
# 합하면 레벨 덧셈
# 인접한 카드 중 가장 큰 것끼리 접합함

N = int(input())
cards = list(map(int,input().split()))
gold = 0
while len(cards) > 1:
    max_num = max(*cards)
    max_num_idx = cards.index(max_num)
    # print('cards', cards,'gold',gold)
    if len(cards) >= 2:
        if max_num_idx == 0:
            gold += cards.pop(max_num_idx+1)
        elif max_num_idx == len(cards)-1:
            gold += cards.pop(max_num_idx-1)
        else:
            if cards[max_num_idx-1] > cards[max_num_idx+1]:
                gold += cards.pop(max_num_idx-1)
            else:
                gold += cards.pop(max_num_idx+1)
    gold += max_num

# print(cards)
print(gold)