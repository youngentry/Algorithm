import sys
input = sys.stdin.readline

m,n = map(int,input().split())
cut_count = int(input())

row = [0,n]
col = [0,m]
for i in range(cut_count):
    dir, num = map(int,input().split())
    if dir == 0:
        row.append(num)
    else:
        col.append(num)

sorted_row = sorted(row)
sorted_col = sorted(col)

max_width = 0
max_height = 0

for i in range(1,len(sorted_row)):
    # print(sorted_row[i],sorted_row[i-1])
    if max_width < sorted_row[i] - sorted_row[i-1]:
        max_width = max(max_width,sorted_row[i] - sorted_row[i-1]) 
for i in range(1,len(sorted_col)):
    if max_height < sorted_col[i] - sorted_col[i-1]:
        max_height = max(max_height,sorted_col[i] - sorted_col[i-1]) 

# print(max_height,max_width)
print(max_height*max_width)