from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")


def bfs(x, y):
    """ x, y : 탐색을 시작할 위치 """
    global visited, maps

    queue = deque([(x, y)])
    visited[x][y] = 1
    answer = 0

    if maps[x][y] == 0:
        answer = 1
    else:
        answer = -2

    while queue:
        nowPos = queue.popleft()

        for i in range(4):
            nx = nowPos[0] + dx[i]
            ny = nowPos[1] + dy[i]

            if 0 <= nx < n  and  0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] != 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    
                    if maps[nx][ny] == 0:
                        answer += 1
                    else:
                        answer -= 2

    else:
        return answer


if __name__ == "__main__":
    n, m = list(map(int, s.readline().rstrip().split(" ")))
    maps = [list(map(int, s.readline().rstrip().split(" "))) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_value = 0;

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 1 :
                visited = [([0] * m) for _ in range(n)]
                score = bfs(i, j)
                max_value = max(max_value, score)

    print(max_value)