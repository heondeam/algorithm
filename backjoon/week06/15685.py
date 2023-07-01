from sys import stdin as s
s = open("input.txt", "rt")

""" 15685. 드래곤 커브 """

# k세대 드래곤 커브 -> k-1세대 드래곤 커브를 끝점 기준으로 90도 시계 방향 회전 후 끝점에 붙이기.

# 크기가 100 * 100인 격자 위에 드래곤 커브가 N개 존재함.
# 이 때 크기가 1 * 1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구해라


if __name__ == "__main__":
    # 드래곤 커브의 개수
    n = int(s.readline().rstrip())
    # 드래곤 커브 x, y, d, g
    curves = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]

    print(curves)