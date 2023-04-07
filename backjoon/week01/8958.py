from sys import stdin as s

s = open("input.txt", "rt")

""" 

문제

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

"""

input_list = s.readlines()

n = int(input_list[0])

del input_list[0]

result = input_list

for i in range(n):
    now_result = [ str(a) for a in result[i].split("\n")[0]]
    point = 0 # 현재 포인트
    sum_point = 0 # 최종 포인트

    for j in range(len(now_result)):
        if now_result[j] == 'O':
            point += 1
            sum_point += point
        else:
            point = 0

    print(sum_point)


