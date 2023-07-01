from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
"""
n, b = map(int, s.readline().rstrip().split())
A = []

for _ in range(n):
    A.append(list(map(int, s.readline().rstrip().split())))

# 행렬 곱하기 알고리즘
def mul(n, a, b):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    
    return result

# 1629 곱셈 문제 참조
def cal(n, b, A):
    if b == 1:
        return A
    # 단순한 2제곱일 경우
    elif b == 2:
        return mul(n, A, A)
    else:
        temp = cal(n, b // 2, A)
        if b % 2 == 0:
            # b가 짝수일 경우 제곱수를 계속 곱한다.
            return mul(n, temp, temp)
        elif b % 2 != 0:
            # b가 홀수일 경우 마지막에 A를 곱해준다.
            return mul(n, mul(n, temp, temp), A)

result = cal(n, b, A)

for row in result:
    for num in row:
        print(num % 1000, end= " ")
    print()