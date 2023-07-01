from sys import stdin as s

s = open("input.txt", "rt")
""" 2780. 비밀번호 """

# 석원이 집의 비밀번호를 풀자
# 1. 비밀번호의 길이는 N이다.
# 2. 비밀번호는 위 그림에 나온 번호들을 눌러서 만든다.
# 3. 비밀번호에서 인접한 수는 실제 위 기계의 번호에서도 인접해야 한다.

# 각 테스트 케이스에 대해서 조건을 만족하는 비밀번호의 개수를 출력하자. (비밀번호를 1234567로 나눈 나머지를 출력)


# def dfs(s, l, data = []) :
#     global answer

#     if len(data) >= l:
#         if data not in answer:
#             answer.append(data)
#         return

#     for i in range(len(machine[s])):
#         dfs(machine[s][i], l, data + [machine[s][i]])

if __name__== "__main__":
    t = int(s.readline().rstrip())
    cases = [int(s.readline().rstrip()) for _ in range(t)]
    maxCase = max(cases)

    # 완전 탐색? 가능한 모든 비밀번호의 개수를 출력 -> dfs 사용 -> 시간 초과
    # dp? 

    dp = [[0] * 10 for _ in range(maxCase + 1)]

    machine = [
        [7],
        [2, 4],
        [1, 3, 5],
        [2, 6],
        [1, 5, 7],
        [2, 4, 6, 8],
        [3, 5, 9],
        [0, 4, 8],
        [5, 7, 9],
        [6, 8]
    ]

    for j in range(0, 10):
        dp[1][j] = 1

    for i in range(2, maxCase + 1):
        for j in range(0, 10):
            new_sum = 0

            for k in range(len(machine[j])):
                new_sum += dp[i-1][machine[j][k]]

            dp[i][j] = new_sum

    for case in cases:
        sum = 0

        for j in range(10):
            sum += dp[case][j]

        print(sum % 1234567)