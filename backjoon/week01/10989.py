from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,0000)이 주어진다. 
둘째 줄부터 N개의 줄에는 수가 주어진다. 
이 수는 절댓값이 10,000보다 작거나 같은 자연수이다.

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
n = int(s.readline())

arr = [0] * 10001

for i in range(n):
    num = int(s.readline())
    arr[num] += 1

for i in range(len(arr)):
    for _ in range(arr[i]):
        print(i)
