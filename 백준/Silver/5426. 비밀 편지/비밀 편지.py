N = int(input())

for _ in range(N):
    letter = input().strip()
    length = len(letter)

    arr = []
    rooted_length = int(length ** 0.5)
    for i in range(rooted_length):
        line = []
        for j in range(rooted_length):
            line.append(letter[i*rooted_length + j])
        arr.append(line)

    temp_arr = [[None]*rooted_length for _ in range(rooted_length)]

    for i in range(rooted_length):
        for j in range(rooted_length):
            temp_arr[j][rooted_length-i-1] = arr[i][j]

    print(''.join([''.join(reversed(row)) for row in reversed(temp_arr)]))

# 00 01 02    02 12 22
# 10 11 12 => 01 11 21
# 20 21 22    00 10 20