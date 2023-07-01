from sys import stdin as s
from sys import maxsize
import heapq

s = open("input.txt", "rt")
""" 
문제

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 
도시의 번호는 1부터 N까지이다.

첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 
둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 
그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 
버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.
출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
"""
def dijkstra(x):
    queue = []
    # 힙에 현재 거리, 노드 형태로 푸쉬 (거리가 가장 짧은 순으로 Pop됨.)
    heapq.heappush(queue, (0, x))
    # 시작 노드의 거리는 0으로
    distances[x] = 0 

    while queue:
        # 현재 노드
        d, v = heapq.heappop(queue)

        # 거리가 d 보다 작다면 볼 필요 없음.
        if distances[v] < d:
            continue

        # 인접한 노드들에 대해서 방문 시작
        for nw, nx in graph[v]:
            # 현재 노드 + 인접 노드까지의 거리
            nd = d + nw

            if  distances[nx] > nd:
                heapq.heappush(queue, (nd, nx))
                distances[nx] = nd

if __name__ == "__main__":
    input_datas = [s.rstrip() for s in s.readlines()]
    n, m = map(int, [input_datas[0], input_datas[1]])
    edges = [list(map(int, s.split())) for s in input_datas[2: m + 2]]
    s, e = list(map(int, input_datas[-1].split()))

    graph = []

    distances= [maxsize] * (n + 1)

    for i in range(n + 1):
        graph.append([])

    for edge in edges:
        v, u, c = edge

        graph[v].append((c, u))

    dijkstra(s)

    print(distances[e])