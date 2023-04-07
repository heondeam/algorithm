from sys import stdin as s

s = open("input.txt", "rt")

n = int(s.readline())

""" 

문제

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

"""

# 중첩 반복문 사용

output = ""

for i in range(0, n):
    for j in range(i + 1):
        output += "*"
    output += "\n"

print(output)