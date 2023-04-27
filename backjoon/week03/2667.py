from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 
문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 
단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. 
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다

첫 번째 줄에는 총 단지수를 출력하시오. 
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""

def BFS(r, c):
    """ r, c : 탐색을 시작할 행, 열 """

    queue = deque([])
    queue.append((r, c))
    visited[r][c] = 1
    house = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 1:
                # 1인 곳에서만 BFS 수행하므로 같다고 생각해도 상관놉
                if maps[x][y] == maps[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    house += 1

    return house

if __name__ == "__main__":
    n = int(s.readline().rstrip())
    maps = []

    # 단지 수
    cnt = 0
    # 단지별 집의 수
    result = []

    for i in range(n):
        maps.append([])
        status = list(map(int, s.readline().rstrip()))
        for j in range(n):
            maps[i].append(status[j])

    visited = [[0] * n for _ in range(n)]

    # 방향 설정 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1 and visited[i][j] != 1:
                result.append(BFS(i, j))
                cnt += 1

    result.sort()
    print(cnt)
    for i in range(len(result)):
        print(result[i])