from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""

if __name__ == "__main__":
    n = int(s.readline().rstrip())


    dp = [0] * 1001

    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5

    if n > 4:
        for i in range(5, n+1):
            dp[i] = dp[i-2] + dp[i-1]

    print(dp[n] % 10007)