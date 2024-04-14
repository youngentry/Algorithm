def ccw(p1,p2,p3):
    x1,x2,x3 = p1[0],p2[0],p3[0]
    y1,y2,y3 = p1[1],p2[1],p3[1]

    # 신발끈 공식
    # x1 x2 x3 x1
    # y1 y2 y3 y1
    AB = (x1*y2 + x2*y3 + x3*y1)
    AC = (y1*x2 + y2*x3 + y3*x1)

    if AB-AC == 0: # 직선
        return 0
    elif AB-AC < 0: # 시계
        return -1
    elif AB-AC > 0: # 반시계
        return 1


p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))

print(ccw(p1,p2,p3))