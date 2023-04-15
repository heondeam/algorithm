from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)
둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.
"""

N, K = list(map(int, s.readline().split()))
numbers = list(map(int, s.readline().rstrip()))

stack = []

for number in numbers:
    while stack and stack[-1] < number and K > 0:
        stack.pop()
        K -= 1
    
    stack.append(number)

if K > 0:
    stack = stack[:-K]

for el in stack:
    print(el, end="")
