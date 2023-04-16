from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

쇠막대기
"""
lines = str(s.readline().rstrip())
stack = []
sum = 0

for i in range(len(lines)):
    if lines[i] == "(":
        stack.append(lines[i])
    else:
        stack.pop()

        if lines[i-1] == "(":
            sum += len(stack)
        else:
            sum += 1

print(sum)