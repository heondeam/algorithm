from sys import stdin as s
import heapq

s = open("input.txt", "rt")

""" 
문제
.
N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

첫째 줄에 행렬 A의 크기 N 과 M이 주어진다. 
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다. 
그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다. 
이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다. 
N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다. 
행렬의 각 원소는 공백으로 구분한다.
"""
input_data = [list(map(int, a.rstrip().split())) for a in s.readlines()]

n, m = input_data[0]
A = input_data[1:n+1]
m2, k = input_data[n+1]
B = input_data[n+2:]

# 3 * 2 행렬과 2 * 3 행렬을 곱하면 3 * 3 행렬이 나온다.
# 즉 N * M 행렬과 M * K 행렬을 곱하면 N * K 행렬이 나옴.
for i in range(n):
    result = []
    for j in range(k):
        a = 0
        for k  in range(m):
            a += A[i][k] * B[k][j]
        result.append(a)
    print(*result)