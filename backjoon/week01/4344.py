from sys import stdin as s

s = open("input.txt", "rt")

""" 

문제

대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

"""

n = [str(a) for a in s.readlines()]

loop_num = int(n[0])

del n[0]

for i in range(loop_num) :
    # 테스트 케이스를 제외한 둘째줄 부터 배열화
    arr = n[i].split(" ")
    # 학생 수
    students_num = int(arr[0])
    del arr[0]

    total = 0

    fine_student = 0

    # 학생 수 만큼 반복하면서 평균 계산
    for j in range(len(arr)):
        total += int(arr[j])

    sum = total // students_num

    for j in range(len(arr)):
        if(int(arr[j]) > sum):
            fine_student += 1

    answer = fine_student / students_num * 100

    print(f'{answer:.3f}%')


