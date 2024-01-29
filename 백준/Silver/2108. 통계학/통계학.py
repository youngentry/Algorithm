import sys

input = sys.stdin.readline

n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

def get_average(num):
    print(round(sum(num)/n))
def get_mid(num):
    print(list(sorted(num))[n//2])
def get_prequent(num):
    counts = {}
    for num in numbers:
        if counts.get(num) == None:
            counts[num] = 1
        else:
            counts[num] += 1

    result = counts.items()

    sorted_result = list(sorted(result, key=lambda x: (-x[1], x[0])))

    if len(sorted_result) >= 2 and sorted_result[0][1]==sorted_result[1][1]:
        print(sorted_result[1][0])
    else:
        print(sorted_result[0][0])

def get_diff(num):
    sor = list(sorted(num))
    min, max = sor[0], sor[-1]
    print(max-min)

get_average(numbers)
get_mid(numbers)
get_prequent(numbers)
get_diff(numbers)