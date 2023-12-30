# n 스위치 100개이하
# switches 0,1 스위치 상태
# students 학생수
# gender, number

n = int(input())
switches = list(map(int,input().split()))
students = int(input())

for i in range(int(students)):
    # print(switches)

    gender, number = map(int,input().split())
    # print(n,switches,students,gender,number)
    
    # 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다
    if gender==1:
        for j in range(1,len(switches)+1):
            if j%number==0:
                switches[j-1] = not switches[j-1]

    # 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 
    # 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
    # 그 구간에 속한 스위치의 상태를 모두 바꾼다. 
    # 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
    same_range = -1
    if gender==2:
        for j in range(len(switches)//2):
            if number-1+j<len(switches) and number-1-j>=0:
                if switches[number-1+j] == switches[number-1-j]:
                    same_range +=1
                else:
                    break
    # print(same_range)
    for j in range(number-1-same_range, number+same_range):
        switches[j] = not switches[j]

def transform(number):
    if number==True or number==1:
        return "1"
    else:
        return "0"

final_switches = ((list(map(transform, switches))))

for i in range(len(final_switches)//20+1):
    print(" ".join(final_switches[i*20:(i+1)*20]))

