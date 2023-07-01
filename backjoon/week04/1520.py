from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

<aside>
여행을 떠난 세준이는 지도를 하나 구하였다. 
이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 
한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 
각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.

현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다. 
그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 
위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.

지도가 주어질 때 이와 같이 

제일 왼쪽 위 지점에서 출발하여 
제일 오른쪽 아래 지점까지 
항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

"""
def dfs(x, y):
    """ x, y : 탐색을 시작할 죄표 """

    # 목적지에 도착했다면? 경로를 찾은 것이므로 1을 반환
    if x == m - 1 and y == n - 1:
        return 1
    
    # 이미 방문한 곳이라면 해당 위치까지의 경로의 수를 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 방문한 곳이 아니라면 방문처리 한다.
    dp[x][y] = 0

    # 상, 하, 좌, 우 탐색 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] < maps[x][y]:
            # 다음으로 이동할 위치가 현재 높이보다 낮다면 이동
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

    # global cnt

    # stack = []
    # stack.append((x, y, maps[x][y]))
    # dp[x][y] = 1

    # while stack:
    #     px, py, h = stack.pop()

    #     for i in range(4):
    #         nx = px + dx[i]
    #         ny = py + dy[i]

    #         if 0 <= nx < m and 0 <= ny < n:
    #             if dp[nx][ny] == 0 and maps[nx][ny] < h:
    #                 stack.append((nx, ny, maps[nx][ny]))

    #                 if nx == m-1 and ny == n-1:
    #                     cnt += 1

if __name__ == "__main__":
    m , n = list(map(int, s.readline().rstrip().split()))
    maps = [list(map(int, s.readline().rstrip().split())) for _ in range(m)]

    dp = [[-1] * (n) for _ in range(m)]

    cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(dfs(0, 0))
