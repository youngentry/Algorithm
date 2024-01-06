N,M = map(int,input().split())

matrix1 = []
matrix2 = []

for T_C in range(N):
    T_C = list(map(int,input().split()))
    matrix1.append(T_C)

for T_C in range(N):
    T_C = list(map(int,input().split()))
    matrix2.append(T_C)

for i in range(N):
    for j in range(M):
        matrix1[i][j] += matrix2[i][j]

for row in matrix1:
    print(*row)