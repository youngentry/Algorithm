import sys
input = sys.stdin.readline
from itertools import permutations

def play(inning,who):
    b1, b2, b3 = 0,0,0
    out_cnt = 0
    score = 0
    num_in = nums[inning]
    while True:
        get_score = 0
        
        if num_in[permu[who]] == 0:
            out_cnt += 1
            if out_cnt == 3:
                return (who + 1) % 9, score+get_score
        elif num_in[permu[who]] == 1:
            get_score += b3
            b1, b2, b3 = 1, b1, b2
        elif num_in[permu[who]] == 2:
            get_score += (b2+b3)
            b1, b2, b3 = 0, 1, b1
        elif num_in[permu[who]] == 3:
            get_score += (b1+b2+b3)
            b1, b2, b3 = 0, 0, 1
        elif num_in[permu[who]] == 4:
            get_score += (b1+b2+b3) + 1
            b1, b2, b3 = 0, 0, 0

        who = (who + 1)%9
        score += get_score


N = int(input())
final_score = 0
nums = [list(map(int,input().split())) for _ in range(N)]
acc = 0
for permu in permutations([1,2,3,4,5,6,7,8],8):
    permu = list(permu)
    permu.insert(3,0)

    who = 0
    tmp_acc = 0
    for inning in range(N):
        who, inning_score = play(inning, who)
        tmp_acc += inning_score
    acc = max(acc, tmp_acc)

print(acc)
