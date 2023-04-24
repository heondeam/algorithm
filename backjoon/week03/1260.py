from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 
문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""
def DFS(v):
    global graph

    # 해당 정점에 방문 처리
    markForDfs[v] = 1

    # 해당 노드 출력
    print(v, end=" ")

    # 해당 노드의 인접한 노드들에 대해서 방문 여부 확인 및 재귀적으로 방문 처리
    for s in graph[v]:
        if markForDfs[s] != 1:
            DFS(s)

def BFS(v):
    global graph

    myQueue = deque([v])

    # 탐색할 노드를 큐에 삽입하고 방문 처리한다.
    markForBfs[v] = 1

    # 큐가 빌 때까지 반복한다.
    while myQueue:
        # 큐에서 노드를 꺼내고, 출력한다.
        nowVertex = myQueue.popleft()
        print(nowVertex, end = " ")

        # 아직 방문하지 않은 인접한 원소들(초기 노드 v가 아님.)을 큐에 삽입한다.
        for s in graph[nowVertex]:
            if markForBfs[s] != 1:
                myQueue.append(s)
                markForBfs[s] = 1

if __name__ == "__main__":
    n, m, v = list(map(int, s.readline().rstrip().split()))

    graph = []

    markForDfs = [0] * (n + 1)
    markForBfs = [0] * (n + 1)

    for i in range(0, n + 1):
        graph.append([])

    for i in range(m):
        u, e = list(map(int, s.readline().rstrip().split()))

        graph[u].append(e)
        graph[e].append(u)

        graph[u].sort()
        graph[e].sort()

    DFS(v)
    print()
    BFS(v)
