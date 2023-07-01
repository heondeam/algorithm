from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 
문제

사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 
그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다. 
이 숲에는 고슴도치가 한 마리 살고 있다. 
고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 
비어있는 곳은 '.'로 표시되어 있고, 
물이 차있는 지역은 '*', 
돌은 'X'로 표시되어 있다. 
비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. 
(위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다. 
물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 
물과 고슴도치는 돌을 통과할 수 없다. 
또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 
물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 
고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 
즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 
이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.
"""

def _water():
    global water
    temp_water = [] # 물이 차 있는 지역

    # 물이 차있는 모든 지역을 탐색
    while water:
        x, y = water.popleft()

        # 상 하 좌 우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동한 위치가 범위 내에 있다면
            if 0 <= nx < r and 0 <= ny < c:
                # 이동할 수 있는 곳이면 물이 찬다.
                if maps[nx][ny] == ".":
                    maps[nx][ny] = "*"
                    visited[nx][ny] = -1
                    temp_water.append((nx, ny)) # 물이 찬 지역을 임시 큐에 저장한다.

    # 물이 찰 수 있는 지역이 모두 채워졌다면?
    # 임시 큐에 있는 다음 탐색할 곳을 큐에 추가한다.                
    for a, b in temp_water:
        water.append((a, b))


# 고슴도치의 이동 bfs 탐색
def bfs():
    global queue

    while queue:
        temp_queue = [] # 임시 큐

        # 고슴도치가 이동할 수 있는 모든 곳을 탐색
        while queue:

            x, y = queue.popleft()

            # 물이 아니고 돌이 아니라면
            if maps[x][y] != "*" and maps[x][y] != "X":

                # 상/하/좌/우 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 탐색하는 곳이 범위 내에 있다면
                    if 0 <= nx < r and 0 <= ny < c:

                        # 비버의 굴이라면 비버의 굴까지 걸리는 이동 횟수 리턴
                        if maps[nx][ny] == "D":
                            return visited[x][y] + 1

                        # 비어 있는 곳이고 탐색하지 않은 곳이라면 탐색
                        elif maps[nx][ny] == "." and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1 # 탐색하기까지 걸린 이동 횟수 초기화
                            temp_queue.append([nx, ny]) # 임시 큐에 탐색할 곳을 추가

        # 고슴도치가 현재 이동할 수 있는 곳을 모두 이동했다면
        # 임시 큐에 있는 다음 탐색할 곳을 큐에 추가
        for a, b in temp_queue:
            queue.append([a, b])

        # 물이 차있는 지역 증가
        _water()

    # 고슴도치가 목적지까지 이동할 수 없다면 "KAKTUS" 리턴
    return "KAKTUS"



if __name__ == "__main__":
    r, c = list(map(int, s.readline().rstrip().split()))
    maps = [list(map(str, s.readline().strip())) for _ in range(r)]
    visited = [([0] * c) for _ in range(r)]

    queue = deque([])
    water = deque([])

    # 고슴도치의 이동 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(r):
        for j in range(c):
            if maps[i][j] == "S":
                queue.append([i, j])
            elif maps[i][j] == "*":
                water.append([i, j])

    # bfs 탐색
    print(bfs())