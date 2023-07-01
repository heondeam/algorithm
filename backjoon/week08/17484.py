from sys import stdin as s

s = open("input.txt", "rt")
""" 17484. 진우의 달 여행 """

# 지구와 우주 사이는 N * M 행렬로 나타낼 수 있다.
# 각 원소의 값은 우주선이 그 공간을 지날 때 소모되는 연료의 양
# 진우의 우주선 특징
# 1. 지구 -> 달로 갈때 움직일 수 있는 방향은 아래 세방향
# 2. 우주선은 전에 움직인 방향으로 움직일 수 없음. (같은 방향으로 두 번 이상 움직일 수 없다.)
# 최대한 연료를 아끼면서 달에 도착하고 싶다. 연료의 최솟값을 구하자.

def dfs(x, y, d, sum = 0):
    global n, matrix

    if y < 0 or y >= m:
        return

    if x == n:
        ans.append(sum)
        return
    
    if d == 0:
        # 왼쪽으로 이동했을 시에
        dfs(x + 1, y, 1, sum + matrix[x][y])
        dfs(x + 1, y + 1, 2, sum + matrix[x][y])
    elif d == 1:
        # 가운데로 이동했을 시에
        dfs(x + 1, y - 1, 0, sum + matrix[x][y])
        dfs(x + 1, y + 1, 2, sum + matrix[x][y])
    elif d == 2:
        # 오른쪽으로 이동했을 시에
        dfs(x + 1, y - 1, 0, sum + matrix[x][y])
        dfs(x + 1, y, 1, sum + matrix[x][y]) 
    elif d == -1:
        dfs(x + 1, y - 1, 0, sum + matrix[x][y])
        dfs(x + 1, y, 1, sum + matrix[x][y])
        dfs(x + 1, y + 1, 2, sum + matrix[x][y]) 


if __name__ == "__main__": 
    n, m = list(map(int, s.readline().rstrip().split()))
    matrix = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]

    # 연료값
    ans = []

    # 아이디어
    # 첫번째 열에서 좌표 선택 후 
    # 3 방향으로 각각 탐색을 진행한다 DFS
    # 이전에 골랐던 방향을 기록해두고
    # 다음번 탐색에서는 다른 방향으로 가게끔 설정하자(좌하향 : 0, 하향 : 1, 우하향 : 2)
    # 다음 위치로 갈때마다 원소값을 더해서 최종 원소값을 저장해두고
    # 그중에서 최솟값을 출력한다.

    for i in range(m):
        dfs(0, i, -1)


    print(min(ans))