from sys import stdin as s
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

s = open("input.txt", "rt")
""" 
문제

아침 산책을 즐기는 서현이는 서울과학고에 입학해서도 아침 산책을 즐기려고 합니다. 
서현이는 산책을 위해 서울과학고의 지리를 분석했고, 그 결과 서울과학고를 
N개의 장소를 N-1개의 길이 잇는 트리 형태로 단순화시킬 수 있었습니다. 
트리 구조이므로, 모든 장소를 몇 개의 길을 통해 오고갈 수 있습니다.

아침 산책은 시작점과 도착점을 정하고, 
시작점에서 도착점까지 트리 위의 단순 경로(같은 점을 여러 번 지나지 않는 경로)를 따라 걷게 됩니다. 
트리 위의 두 점 사이의 경로는 유일하므로 시작점과 도착점이 정해지면 경로는 유일하게 결정됩니다.

N개 장소 중에 일부 장소는 실내이며, 나머지 장소는 실외입니다. 
서현이는 산책을 시작하기 전부터 운동을 하는 것을 원치 않기 때문에, 산책의 시작점과 끝점은 모두 실내여야 합니다. 
또한, 산책 도중에 실내 장소를 만나면 산책을 그만두고자 하는 욕구가 생기기 때문에, 
산책 경로 위에 시작점과 끝점을 제외하고 실내 장소가 있으면 안 됩니다.

서현이는 매일 다른 산책 경로를 걷고자 합니다. 서로 다른 산책 경로가 몇 가지 있는지 구해 봅시다.

첫 줄에는 정점의 수 N이 주어집니다.

둘째 줄에는 1과 0으로 이루어진 길이 N의 문자열 A가 주어집니다. 
i번째 문자 A_i가 1일 경우 i번 장소는 실내이며,
0인 경우 i번 장소는 실외입니다.

셋째 줄부터 N+1번 줄까지는 
i+2번 줄에 트리의 각 간선을 나타내는 두 정수 u_i, v_i가 주어집니다. 
이는 i번째 간선이 u_i번 정점과 v_i번 정점을 연결한다는 의미입니다.
"""
def DFS(v):
    """ v : 정점의 번호 """
    indoor = 0

    visited[v] = 1

    for i in graph[v]:
        # 실외일 경우
        if A[i] == 0:
            # 방문하지 않았다면
            if visited[i] == 0:
                visited[i] = 1
                indoor += DFS(i)
        else: 
            indoor += 1

    return indoor


if __name__ == "__main__":
    n = int(s.readline().rstrip()) # 노드의 수
    A = [0] + list(map(int, s.readline().rstrip())) # 노드 n에 대해서 A[n-1]이 1이면 실내, 0이면 실외
    edges = [list(map(int, s.readline().rstrip().split())) for _ in range(n - 1)]
    graph = []

    cnt = 0

    for i in range(n + 1):
        graph.append([])

    for edge in edges:
        u, e = edge

        graph[u].append(e)
        graph[e].append(u)

        # 실내끼리 인접했을 경우 경로를 2개 더해줌.
        if A[u] == 1 and A[e] == 1:
            cnt += 2

    visited = [0] * (n + 1)

    for i in range(1, n + 1):
        indoor = 0

        # 실외를 기준으로 DFS 수행
        if A[i] != 1:
            if visited[i] == 0:
                indoor = DFS(i)

        cnt += indoor * (indoor - 1)

    print(cnt)