import sys

input = sys.stdin.readline

q1 = []
q2 = []

# q1에 추가
def push_(num):
    q1.append(num)

# q2에서 pop
def pop_():
    # 큐에 들어있는 정수가 없으면 -1 출력
    if not len(q1) and not len(q2):
        print(-1)
        return

    # q2가 비어있으면 q2에 추가
    if not len(q2):
        while len(q1):
                q2.append(q1.pop())
    
    # q2에서 pop
    popped =q2.pop()
    print(popped)

def size_():
    print(len(q1)+len(q2))

def empty_():
    if len(q1)+len(q2)==0:
        print(1)
    else:
        print(0)

def front_():
    if len(q1)+len(q2)==0:
        print(-1)
        return

    if len(q2):
        print(q2[-1])
    else:
        print(q1[0])

def back_():
    if len(q1)+len(q2)==0:
        print(-1)
        return

    if len(q1):
        print(q1[-1])
    else:
        print(q2[0])

T = int(input().strip())

for _ in range(T):
    line = input().split()
    order, number = None, None
    if line[0] == 'push':
        order, number = line[0], int(line[1])
    else:
        order = line[0]

    if order == "push":
        push_(number)
    elif order == "pop":
        pop_()
    elif order == "size":
        size_()
    elif order == "empty":
        empty_()
    elif order == "front":
        front_()
    elif order == "back":
        back_()