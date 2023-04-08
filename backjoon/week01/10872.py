from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
"""

n = int(s.readline())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(n))











