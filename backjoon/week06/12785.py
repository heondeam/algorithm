from sys import stdin as s

s = open("input.txt", "rt")

""" 12785. 토쟁이의 등굣길 """
if __name__ == "__main__":
    # y축과 평행한 w개 도로, x축과 평행한 h개 도로
    w, h = list(map(int, s.readline().rstrip().split()))
    # 토스트 가게 죄표
    x, y = list(map(int, s.readline().rstrip().split()))

    maps = [[0] * (w + 1) for _ in range(h + 1)]

    maps[1][1] = 1

    # 토쟁이의 집 maps[1][1]
    # 토스트 집 위치 maps[x][y]
    # 학교의 위치 maps[h][w]

    # 토스트 가게 까지의 경로의 수
    for i in range(1, y+1):
        for j in range(1, x+1):
            if i > 1 :
                maps[i][j] += maps[i-1][j]
            if j > 1:
                maps[i][j] += maps[i][j-1]

    # 학교까지의 경로의 수
    for i in range(y, h + 1):
        for j in range(x, w+1):
            if i > y :
                maps[i][j] += maps[i-1][j]
            if j > x:
                maps[i][j] += maps[i][j-1]

    print((maps[h][w]) % 1000007)