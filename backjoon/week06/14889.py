from sys import stdin as s
from itertools import combinations

s = open("input.txt", "rt")
""" 14889. 스타트와 링크 """

def dfs(s):
    """ s: 탐색을 시작할 노드 """
    global n

    stack = []
    stack.append(s)

    visited = [0] * (n + 1)
    visited[s] = 1

    ans = []

    while stack:
        now_node = stack.pop()

        for _ in range((n // 2) - 1):
            if visited[now_node + 1] == 0:
                stack.append(now_node + 1)
                visited[now_node + 1] = 1
                ans.append((s, now_node))

if __name__ == "__main__":
    n = int(s.readline().rstrip())
    S = [list(map(int, s.readline().rstrip().split())) for _ in range(n)]


    result = []

    dfs(1)