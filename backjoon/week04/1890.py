from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

N×N 게임판에 수가 적혀져 있다. 
이 게임의 목표는 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프를 해서 가는 것이다.

각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다. 
반드시 오른쪽이나 아래쪽으로만 이동해야 한다. 
0은 더 이상 진행을 막는 종착점이며, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야 한다. 
한 번 점프를 할 때, 방향을 바꾸면 안 된다. 
즉, 한 칸에서 오른쪽으로 점프를 하거나, 아래로 점프를 하는 두 경우만 존재한다.

가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 게임 판의 크기 N (4 ≤ N ≤ 100)이 주어진다.
그 다음 N개 줄에는 각 칸에 적혀져 있는 수가 N개씩 주어진다. 
칸에 적혀있는 수는 0보다 크거나 같고, 9보다 작거나 같은 정수이며, 
가장 오른쪽 아래 칸에는 항상 0이 주어진다.

가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 문제의 규칙에 맞게 갈 수 있는 경로의 개수를 출력한다. 
경로의 개수는 263-1보다 작거나 같다.
"""

# def bfs(x, y):
#     """x, y: 탐색을 시작할 좌표"""
#     global ans

#     queue = deque()
#     queue.append((x, y, maps[x][y]))
#     visited[x][y] = 1

#     path = (x, y, maps[x][y])

#     while queue:
#         v = queue.popleft() # 현재 노드

#         for i in range(2):
#             nx = v[0] + dx[i]
#             ny = v[1] + dy[i]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     queue.append((nx, ny, maps[nx][ny]))

#                     if nx == path[0] + path[2] or ny == path[0] + path[2]:
#                         path = (nx, ny, maps[nx][ny])
#                         ans.append((nx, ny, maps[nx][ny]))


if __name__ == "__main__":
    n = int(s.readline().rstrip())
    maps = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]

    # dp 테이블 의미. dp[i][j] = i,j로 가는 경로의 수
    dp = [[0] * (n) for _ in range(n)]

    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            posPosition = maps[i][j]

            if posPosition > 0:
                if i + posPosition >= 0 and i+ posPosition < n:
                    dp[i + posPosition][j] += dp[i][j]

                if j + posPosition >= 0 and j+ posPosition < n:
                    dp[i][j + posPosition] += dp[i][j]

    print(dp[-1][-1])

    # ans = []

    # dx = [1, 0]
    # dy = [0, 1]

    # bfs(0, 0)

