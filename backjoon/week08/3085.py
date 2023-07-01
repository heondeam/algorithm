from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 3085. 사탕 게임 """

# n * n 크기에 사탕을 채워 놓는다.
# 사탕의 색이 다른 인접한 두 칸을 고른다.
# 고른 칸에 들어있는 사탕을 서로 교환한다.
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고른다음에 그 사탕을 모두 먹는다.
# 상근이가 먹을 수 있는 사탕의 최대 개수는?
# 사탕의 색깔 C , P , Z , Y


def check_w():
    global candy
    
    for k in range(n):
        cnt_row = 1

        for l in range(n - 1):
            if board[k][l] == board[k][l + 1]:
                cnt_row += 1
                candy = max(cnt_row, candy)
            else:
                cnt_row = 1

def check_h():
    global candy

    for k in range(n):
        cnt_col = 1

        for l in range(n - 1):
            if board[l][k] == board[l + 1][k]:
                cnt_col += 1
                candy = max(cnt_col, candy)
            else:
                cnt_col = 1


if __name__ == "__main__":
    n = int(s.readline().rstrip())
    board = [list(s.readline().rstrip()) for _ in range(n)]

    candy = 0

    # 아이디어
    # 사탕의 색이 다른 인접한 두 칸을 모두 골라서 사탕을 교환한다.



    for i in range(n):
        for j in range(n-1):
            if board[i][j] != board[i][j + 1]:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                check_w()
                check_h()
                board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1]

            if board[j][i] != board[j + 1][i]:
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
                check_w()
                check_h()
                board[j+1][i], board[j][i] = board[j][i], board[j+1][i]


    print(candy)