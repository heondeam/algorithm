from sys import stdin as s

s = open("input.txt", "rt")

""" 

문제

9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

"""

input_list = [int(a) for a in s.readlines()]

highest_num = 0;
now_index = 0;

for i in range(len(input_list)):
    if(input_list[i] > highest_num):
        highest_num = input_list[i]
        now_index = i

print(str(highest_num) + "\n" + str(now_index + 1))

