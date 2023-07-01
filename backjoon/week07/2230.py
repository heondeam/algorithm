from sys import stdin as s
from sys import maxsize
from itertools import combinations

s = open("input.txt", "rt")
""" 2230. 수 고르기 """


def find_answer():
    global A, n, m, ans

    lt = 0
    rt = 1

    while lt < n and rt < n:
        if A[rt] - A[lt] < m:
            rt += 1
        else:
            ans = min(ans, A[rt] - A[lt])
            lt += 1

    print(ans)



if __name__ == "__main__":
    n, m = list(map(int, s.readline().rstrip().split()))
    A = [int(s.readline().rstrip()) for _ in range(n)]
    A.sort()

    ans = maxsize

    find_answer()