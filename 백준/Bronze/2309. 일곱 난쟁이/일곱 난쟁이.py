lists = [int(input()) for _ in range(9)]
lists.sort()

height_sum = sum(lists)

found = False
for i in range(9):
    if found:
        break
    for j in range(i+1, 9):
        if height_sum - lists[i] - lists[j] == 100:
            fake1, fake2 = lists[i], lists[j]
            found = True
            break

answer = [dwarf for dwarf in lists if dwarf != fake1 and dwarf != fake2]

for height in answer:
    print(height)