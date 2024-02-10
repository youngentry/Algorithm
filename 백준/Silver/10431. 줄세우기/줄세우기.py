import sys
input = sys.stdin.readline

# 키순서 번호
# 항상 20명
# 같은 키 없음

# 아무나 맨 앞에 세움
# 자기보다 앞에 큰 학생 없으면 그냥 끝
# 앞에 큰 학생 한 명 이상 있으면 그 중 가장 앞 A에 섬
# A부터 뒤의 모든 학생들은 공간을 만들기 위해 한발 물러섬

# insert한 지점+1~끝까지 count++

t = int(input())
for tc in range(t):
    p, *numbers = map(int,input().split())
    n = 20
    count = 0
    arr =[]
    # 버블정렬로 자리바꾸기 할 때마다 count
    for i in range(n):
        arr.append(numbers[i])
        cur = arr[i]
        for j in range(0,i):
            if arr[j] > cur:
                popped = arr.pop(i)
                arr.insert(j,cur)
                count += len(arr[j+1:])
                # print(len(arr[j+1:]))
                break
        # print(arr)
    print(f'{p} {count}')
