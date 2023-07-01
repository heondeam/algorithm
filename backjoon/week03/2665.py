from sys import stdin as s
from sys import maxsize
import heapq


s = open("input.txt", "rt")
""" 
문제

n×n 바둑판 모양으로 총 n2개의 방이 있다. 일부분은 검은 방이고 나머지는 모두 흰 방이다. 
검은 방은 사면이 벽으로 싸여 있어 들어갈 수 없다. 
서로 붙어 있는 두 개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다. 
윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고, 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방이다.
시작방에서 출발하여 길을 찾아서 끝방으로 가는 것이 목적인데, 
아래 그림의 경우에는 시작방에서 끝 방으로 갈 수가 없다. 
부득이 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.
아래 그림은 n=8인 경우의 한 예이다.
위 그림에서는 두 개의 검은 방(예를 들어 (4,4)의 방과 (7,8)의 방)을 흰 방으로 바꾸면,
시작방에서 끝방으로 갈 수 있지만, 어느 검은 방 하나만을 흰 방으로 바꾸어서는 불가능하다. 
검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성하시오.
단, 검은 방을 하나도 흰방으로 바꾸지 않아도 되는 경우는 0이 답이다.

첫 줄에는 한 줄에 들어가는 방의 수 n(1 ≤ n ≤ 50)이 주어지고, 
다음 n개의 줄의 각 줄마다 0과 1이 이루어진 길이가 n인 수열이 주어진다. 
0은 검은 방, 1은 흰 방을 나타낸다.

첫 줄에 흰 방으로 바꾸어야 할 최소의 검은 방의 수를 출력한다.
"""
def BFS(x, y):
    """ x, y 탐색을 시작할 위치 """
    global rooms

    myHeap = []
    # 출발점 푸쉬 (카운트, x좌표, y좌표)
    heapq.heappush(myHeap, (0, x, y))
    visited[x][y] = 1

    while myHeap:
        count, cx, cy = heapq.heappop(myHeap)

        # 도착 지점에 도착했을 경우 (7, 7) 좌표
        if cx == (n - 1) and cy == (n - 1):
            return count
        
        # 상하좌우로 한칸씩 이동하면서 탐색을 진행한다.
        for i in range(4):
            nx = cx + pos[i][0]
            ny = cy + pos[i][1]

            # 좌표가 범위를 벗어나지 않고 해당 좌표의 방에 방문한 적이 없다면
            if (0 <= nx < n) and (0 <= ny < n) and visited[nx][ny] != 1:
                # 방문 처리
                visited[nx][ny] = 1

                # 흰 방일 경우
                if rooms[nx][ny] == 1:
                    heapq.heappush(myHeap, (count, nx, ny))

                # 검은 방
                else:
                    heapq.heappush(myHeap, (count + 1, nx, ny))

def dijkstra(r, c):
    """ r, c 탐색을 시작할 좌표 (행, 열) """

    myheap = []
    heapq.heappush(myheap, (0, r, c))
    visited[r][c] = 1

    while myheap:
        count, nr, nc = heapq.heappop()

        if r == n - 1 and c == n - 1:
            return count

        for i in range(4):
            rs = nr + pos[i][0] 
            cs = nc + pos[i][1]

            if 0 < rs < n and 0 < cs < n and distances[rs][cs] < 








if __name__ == "__main__":
    n = int(s.readline().rstrip())
    rooms = [list(map(int, s.readline().rstrip())) for _ in range(n)]

    # 4방향 설정 상하좌우
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 방문여부 체크를 위한 리스트
    visited = [[0] * n for _ in range(n)]