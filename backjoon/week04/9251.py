from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 
문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
"""


if __name__ == "__main__":
    x = list(s.readline().rstrip())
    y = list(s.readline().rstrip())

    dp = [([0] * (len(y) + 1)) for _ in range(len(x) + 1)]

    maxValue = 0

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            if dp[i][j] > maxValue:
                maxValue = dp[i][j]
    else:
        print(maxValue)