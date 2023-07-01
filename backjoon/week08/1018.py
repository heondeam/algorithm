from sys import stdin as s

s = open("input.txt", "rt")
""" 1018. 체스판 다시 칠하기 """

if __name__ == "__main__":
    n, m = list(map(int, s.readline().rstrip().split()))
    board = [list(s.readline().rstrip()) for _ in range(n)]

    repair = []

    for i in range(n):
        for j in range(m):
            if i + 8 > n or j + 8 > m:
                break
            else:
                first_W = 0
                first_B = 0

                for k in range(i, i + 8):
                    for l in range(j, j + 8):
                        if (k + l) % 2 == 0:
                            if board[k][l] != "W":
                                first_W += 1
                            if board[k][l] != "B":
                                first_B += 1
                        else:
                            if board[k][l] != "B":
                                first_W += 1
                            if board[k][l] != "W":
                                first_B += 1

                repair.append(min(first_B, first_W))


    print(min(repair))