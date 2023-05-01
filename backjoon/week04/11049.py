from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다. 
행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.

AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번이다.
BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36 + 90 = 126번이다.
같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

행렬 N개의 크기가 주어졌을 때, 
모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 
입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.
둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)
항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 
정답은 231-1 보다 작거나 같은 자연수이다. 
또한, 최악의 순서로 연산해도 연산 횟수가 231-1보다 작거나 같다.
"""


def dpFunc(start, end):
    if dp[start][end] != 0:
        # 이미 계산되어 있으면 그 값을 리턴함.
        return dp[start][end]
    if start == end:
        # 행렬 1부터 행렬 1까지의 곱셈 연산 횟수는 0이므로
        return 0
   
    # 결과값을 초기화 (inf로 초기화하여 최솟값을 갱신해 나갈것)
    ans = float('inf')

    for i in range(start, end):
        temp = dpFunc(start, i) + dpFunc(i+1, end) + sizes[start][0] * sizes[end][0] * sizes[end][1]

        if ans > temp:
            ans = temp

    dp[start][end] = ans
    return ans

if __name__ == "__main__":
    n = int(s.readline().rstrip())
    sizes = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]

    dp = [[0] * (n) for _ in range(n)]

    # 인접 행렬의 곱셈 연산 횟수는 미리 계산
    for i in range(n-1):
        dp[i][i+1] = sizes[i][0] * sizes[i+1][0] * sizes[i+1][1]

    # dp[i][j] = 행렬 i부터 j까지 곱했을 때 최소 연산 횟수
    # 그러니까 우리는 dp[1][3] = 행렬 1부터 3까지 곱했을 때 최소 연산 횟수를 구해야 한다.
    # dp[1][3] = dp[1][k] + dp[k+1][3] + pi*pk+1*pj+1

    print(dpFunc(0, n-1))