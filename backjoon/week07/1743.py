from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 1743. 음식물 피하기 """

def bfs(x, y):
    global size

    queue = deque([])
    queue.append((x, y))

    while queue:
        nx, ny = queue.popleft()

        for i in range(4):
            sx = nx + dx[i]
            sy = ny + dy[i]

            if 0 < sx <= N and 0 < sy <= M and visited[sx][sy] == 0:
                if maps[sx][sy] == 1:
                    queue.append((sx, sy)) 
                    visited[sx][sy] == 1
                    size += 1

if __name__ == "__main__":
    N, M, K = list(map(int, s.readline().rstrip().split()))
    pos = [list(map(int, s.readline().rstrip().split())) for _ in range(K)]
    maps = [[0] * (M + 1) for _ in range(N + 1)]
    maxValue = 0

    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]

    for p in pos:
        maps[p[0]][p[1]] = 1

    for p in pos:
        visited = [[0] * (M + 1) for _ in range(N + 1)]
        size = 0
        bfs(p[0], p[1])
        maxValue = max(maxValue, size)

    print(maxValue)