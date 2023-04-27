from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 
문제

형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 
형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 
나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 
방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.

이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 
만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고,
두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.

첫째 줄에 방 바닥의 세로 크기N과 가로 크기 M이 주어진다. 
둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 
이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다. 
N과 M은 50 이하인 자연수이다.
"""

def BFS(r, c):
    """ r, c 탐색을 시작할 행과 열 """
    queue = deque([])
    queue.append((r, c))
    visited[r][c] = 1

    while queue:
        x, y = queue.popleft()

        # 방문 체크
        visited[x][y] = 1

        # 장식 모양이 "-" 일 때는 옆으로만 이동
        if boards[x][y] == "-":
            if y + 1 < m and boards[x][y+1] == "-":
                queue.append((x, y+1))
        # 장식 모양이 "|" 일 때는 아래로만 이동    
        elif boards[x][y] == "|":
            if x + 1 < n and boards[x+1][y] == "|":
                queue.append((x+1, y))

if __name__ == "__main__":
    n, m = list(map(int, s.readline().rstrip().split()))
    boards = []
    cnt = 0

    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        boards.append([])
        quticles = s.readline().rstrip()
        for j in range(m):
            boards[i].append(quticles[j])

    for i in range(n):
        for j in range(m):
            if visited[i][j] != 1:
                # 방문하지 않은 모든 위치에서 BFS수행. 각각 BFS 돌면서 방문 가능한 곳은 1로 바뀜
                BFS(i, j)
                cnt += 1

    print(cnt)