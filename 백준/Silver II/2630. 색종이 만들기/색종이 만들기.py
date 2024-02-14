import sys
input = sys.stdin.readline

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int,input().split())))

a_paper = 0
b_paper = 0

def divide(s_grid,size):
    global a_paper
    global b_paper

    a_count = 0
    b_count = 0

    # print(*s_grid)
    for i in range(size):
        for j in range(size):
            if s_grid[i][j] == 1:
                a_count += 1
            else:
                b_count += 1
    # print(*s_grid,sep='\n')
    # print(a_count,b_count, size)
    if a_count == size**2:
        a_paper+=1
        return
    if b_count == size**2:
        b_paper+=1
        return

    # print(size,size//2)
    s1=[]
    s2=[]
    s3=[]
    s4=[]

    for i in range(size):
        # print(i)
        # print(s_grid[i])
        if i<size//2:
            s1.append(s_grid[i][:size//2])
            s2.append(s_grid[i][size//2:])
        if i>=size//2:
            s3.append(s_grid[i][:size//2])
            s4.append(s_grid[i][size//2:])

    # print('-------')
    # print(*s1,sep='\n')
    # print('-------')
    # print(*s2,sep='\n')
    # print('-------')
    # print(*s3,sep='\n')
    # print('-------')
    # print(*s4,sep='\n')
    # print('-------')

    divide(s1,size//2)
    divide(s2,size//2)
    divide(s3,size//2)
    divide(s4,size//2)

# for i in range(4):
#     for j in range(4):
#         if i<4//2 and j<4//2:
#             print(1,i,j)
#         elif i<4//2 and j>=4//2:
#             print(2,i,j)
#         elif i>=4//2 and j>=4//2:
#             print(3,i,j)
#         elif i>=4//2 and j<4//2:
#             print(4,i,j)


divide(grid,n)

print(b_paper)
print(a_paper)