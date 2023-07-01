from sys import stdin as s

s = open("input.txt", "rt")

""" 17144. 미세먼지 안녕! """

# 집의 크기 R * C
# (r, c) = r행 c열
# 공기 청정기는 항상 1번 열에만 설치되어 있음. 크기는 2행을 차지함 (2 * 1)
# 미세먼지의 양 A[r][c], 
# 확산되는 미세먼지의 양 A[r][c] / 5 소수점 버림
# 남은 미세먼지의 양 A[r][c] - (A[r][c] / 5) * 확산된 방향 수

# T초가 지난 후에 방에 남아있는 미세먼지의 양을 구하자.

def dust():
    # 네방향으로 확산될 수 있다. 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]    

    tmp_arr = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if A[i][j] != 0 and A[i][j] != -1:
                tmp = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        tmp_arr[nx][ny] += A[i][j] // 5
                        tmp += A[i][j] // 5

                A[i][j] -= tmp 

    for i in range(R):
        for j in range(C):
            A[i][j] += tmp_arr[i][j]      

def air_up():
    global up

    # 반시계방향 순환
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]   

    direct = 0
    before = 0

    x, y = up, 1

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]

        if x == up and y == 0:
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue

        A[x][y], before = before, A[x][y]
        x = nx
        y = ny


def air_down():
    global down

    # 시계방향 순환
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]   

    direct = 0
    before = 0

    x, y = down, 1

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]

        if x == down and y == 0:
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
            
        A[x][y], before = before, A[x][y]
        x = nx
        y = ny



if __name__ == "__main__":
    R, C, T = list(map(int, s.readline().rstrip().split()))
    A = [list(map(int, s.readline().rstrip().split())) for _ in range(R)]

    answer = 0

    # 공기 청정기의 위치 - 공기 청정기는 1열에 위치한다.
    # 행만 구해주면 된다.
    up = -1
    down = -1

    for i in range(R):
        if A[i][0] == -1:
            up = i
            down = i + 1

    for _ in range(T):
        dust()
        air_up()
        air_down()

    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                answer += A[i][j]

    print(answer)