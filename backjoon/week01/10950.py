from sys import stdin as s

s = open("input.txt", "rt")

n = int(s.readline())

arr = [case.rstrip().split() for case in s.readlines()]

""" 
문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""

for i in range(n):
    a, b = int(arr[i][0]), int(arr[i][1])

    print(a + b)