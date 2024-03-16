import sys
input = sys.stdin.readline

N = int(input())

arr = [0]

for i in range(1,10):
    arr.append(i)
    for j in range(i-1,-1,-1):
        arr.append(i*10+j)
        for k in range(j-1,-1,-1):
            arr.append(i*100+j*10+k)
            for p in range(k-1,-1,-1):
                arr.append(i*1000+j*100+k*10+p)
                for q in range(p-1,-1,-1):
                    arr.append(i * 10000 + j * 1000 + k * 100 + p*10 + q)
                    for r in range(q-1,-1,-1):
                        arr.append(i * 100000 + j * 10000 + k * 1000 + p * 100 + q*10 + r)
                        for a in range(r-1,-1,-1):
                            arr.append(i * 1000000 + j * 100000 + k * 10000 + p * 1000 + q*100 + r*10 + a)
                            for b in range(a-1,-1,-1):
                                arr.append(i * 10000000 + j * 1000000 + k * 100000 + p * 10000 + q * 1000 + r * 100 + a*10+b)
                                for c in range(b-1,-1,-1):
                                    arr.append(i * 100000000 + j * 10000000 + k * 1000000 + p * 100000 + q * 10000 + r * 1000 + a * 100 + b*10 + c)
                                    for d in range(c - 1, -1, -1):
                                        arr.append(i * 1000000000 + j * 100000000 + k * 10000000 + p * 1000000 + q * 100000 + r * 10000 + a * 1000 + b * 100 + c*10+d)

# 9876543210
arr.sort()
if N > 1022:
    print(-1)
else:
    print(arr[N])
