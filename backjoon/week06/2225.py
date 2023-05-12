from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 
또한 한 개의 수를 여러 번 쓸 수도 있다.

첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.

"""

if __name__ == "__main__":
    n, k = map(int, s.readline().rstrip().split())

    numbers = [i for i in range(n + 1)]
    cnt = 0


    # dp[k][n] = 0 ~ n 개의 수 중에서 정수 k개를 더해서 n이 되는 경우의 수
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n + 1):
        dp[i][1] = 1

    for i in range(1, k + 1):
        dp[1][i] = i      
    
    for i in range(2, n+1):
        for j in range(2, k+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[n][k] % 1000000000)