from sys import stdin as s

s = open("input.txt", "rt")

input_text = s.readlines()

loop_num = int(input_text[0])

""" 
문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""

# print(input_text)

now_loop_num = 1

while now_loop_num <= loop_num :
    a, b = map(int ,input_text[now_loop_num].split(" "))

    print(a + b)
    now_loop_num += 1

