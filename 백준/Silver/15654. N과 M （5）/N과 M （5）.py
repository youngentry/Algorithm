# 순열은 방문(used)처리를 통해서 
# 이미 사용한 번호를 제외시키고, 나머지를 붙이는 방식으로 구현할 수 있다.

# 배열의 길이(i)가 M과 같다면 해당 배열을 반환하면 된다.

def get_permu(i,M):
    global numbers

    if i == M:
        for num in path:
            print(num,end=' ')
        print()
        return

    for j in range(len(numbers)):
        if used[j] == False:
            used[j] = True
            path.append(numbers[j])
            get_permu(i+1,M)
            path.pop()
            used[j] = False

N,M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
permus = []
path = []
used = [False for _ in range(len(numbers))]

get_permu(0,M)
