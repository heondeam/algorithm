from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

자연수 A를 B번 곱한 수를 알고 싶다. 
단 구하려는 수가 매우 커질 수 있으므로 
이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다.
A, B, C는 모두 2,147,483,647 이하의 자연수이다.

첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
"""
A, B, C = list(map(int, s.readline().split()))

'''
수학의 분배법칙 => 분할정복
10^11 % 12
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
'''
def mul(a,b):
    if b == 1:
        return a % C
    elif b % 2 == 0:
        muldiv = mul(a, b // 2)
        return (muldiv * muldiv) % C
    elif b % 2 != 0:
        muldiv = mul(a, b//2)
        return (muldiv * muldiv * a) % C

print(mul(A, B))