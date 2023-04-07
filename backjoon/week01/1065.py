from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""

# 등차수열 - 연속된 두 개의 수의 차이가 일정한 수열)-
# 한수 - 각 자리의 수가 등차수열을 이룸.

n = int(s.readline())

result = 0


def isHansu(n):
    hansu = 0
    for i in range(1, n+1):
        num_list = list(map(int, str(i)))
        if i < 100: 
            hansu += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            hansu += 1

    return hansu

print(isHansu(n))









