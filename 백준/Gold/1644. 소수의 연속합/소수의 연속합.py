def che(N):
    if N == 1:
        return

    for i in range(2, N+1):
        if i not in num_set:
            primes.append(i)
            num_set.add(i)
            for j in range(i*2,N+1,i):
                num_set.add(j)


N = int(input())
if N == 1:
    print(0)
else:
    # N까지 생성할 수 있는 모든 소수를 에라토스테네스의 체로 구함
    # 투포인터로 연속된 소수들의 합으로 만들어지는지 판별
    primes = []
    num_set = set()
    che(N)

    prime_size = len(primes)
    l,r = 0,0
    acc = primes[0]
    ans = 0
    while True:
        # 작으면 오른쪽 늘리기
        if acc < N and r+1 < prime_size:
            r += 1
            acc += primes[r]
        # 크면 왼쪽 당기기
        elif acc > N and l+1 < prime_size:
            acc -= primes[l]
            l += 1
        # 같으면 추가하고 다음으로:
        if acc == N:
            ans +=1
            if l+1 < prime_size:
                acc -= primes[l]
                l += 1

            if r+1 < prime_size:
                r += 1
                acc += primes[r]

        if r == prime_size-1 and l == prime_size-1:
            break
    print(ans)