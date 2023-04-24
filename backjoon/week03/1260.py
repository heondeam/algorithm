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
# def DFS(s):
#     """ s: 탐색을 시작할 노드 """
#     global markForDfs

#     # 방문한 s를 출력
#     print(s, end=" ")

#     # s에 대해 방문 표시
#     markForDfs[s] = 1

#     # s에 인접한 노드들에 대해 DFS를 재귀적으로 실행
#     # 방문하지 않은 노드들에만 탐색 
#     for i in graph[s]:
#         if markForDfs[i] != 1:
#             DFS(i)
            
# def DFS(s):
#     """ s: 탐색을 시작할 노드 """
#     global markForDfs

#     # DFS 탐색을 위한 스택 생성 및 시작 노드 삽입
#     stackForDfs = [s]

#     # 현재 노드를 방문 표시
#     markForDfs[s] = 1

#     # 스택이 빌 때까지 루프 수행
#     while stackForDfs:
#         # 스택의 맨 위 노드를 팝하고 출력
#         nowVertex = stackForDfs.pop()
#         print(nowVertex, end=" ")

#         # 인접한 노드 중에서 방문하지 않은 노드를 스택에 삽입
#         for i in reversed(graph[nowVertex]):
#             if markForDfs[i] != 1:
#                 stackForDfs.append(i)
#                 markForDfs[i] = 1

def BFS(s):
    """ s: 탐색을 시작할 노드 """
    global markForBfs

    # BFS 탐색을 위한 큐 생성
    # 처음 탐색한 노드를 큐에 푸시 후 방문 표시
    queueForBfs = deque([s])
    markForBfs[s] = 1

    # 큐가 빌 때까지 루프 수행
    while queueForBfs:
        # 탐색한 노드를 큐에서 팝 그리고 출력
        nowVertex = queueForBfs.popleft()
        print(nowVertex, end=" ")

        # 방금 탐색한 노드에 인접한 노드들을 모두 큐에 푸시 후
        # 큐가 빌 때 까지 같은 과정 반복
        for i in graph[nowVertex]:
            if markForBfs[i] != 1:
                queueForBfs.append(i)
                markForBfs[i] = 1

if __name__ == "__main__":
    n, m, v = list(map(int, s.readline().rstrip().split()))

    # 방문 표시를 위한 배열 생성 인덱스 0은 무시하고 1부터 순차적으로 생성
    markForDfs = [0] * (n + 1)
    markForBfs = [0] * (n + 1)

    # 2차원 리스트 형태로 노드와 해당 노드에 인접한 노드들을 표현
    graph = []

    # 편의를 위해 0번 인덱스는 생각하지 않음. 1부터 차례대로 노드
    for i in range(n+1):
        graph.append([])

    for i in range(m):
        u, e = list(map(int, s.readline().rstrip().split()))

        # 노드 v에 대해서 인접한 노드 e를 추가
        graph[u].append(e)
        # 양방향 그래프이기 떄문에 양쪽으로 인접 노드를 표시하기 위해 추가
        graph[e].append(u)

        # 낮은 번호부터 탐색할 것이기 때문에 정렬해줌.
        # graph[u].sort()
        # graph[e].sort()

    DFS(v)
    print()
    BFS(v)