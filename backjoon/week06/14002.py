from sys import stdin as s

s = open("input.txt", "rt")

""" 14002. 가장 긴 증가하는 부분 수열 4 """
if __name__ == "__main__":
    n = int(s.readline().rstrip())
    A = [0] + list(map(int, s.readline().rstrip().split()))

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        leng = 0

        for j in range(i-1, 0, -1):
            if A[j] < A[i] and dp[j] > leng:
                leng = dp[j]

        dp[i] = leng + 1
    

    print(max(dp))

    temp = max(dp)
    result = []

    for i in range(n-1 , -1, -1):
        if dp[i + 1] == temp:
            result.append(A[i + 1])
            temp -= 1
    
    result.reverse()

    print(*result, sep=" ")