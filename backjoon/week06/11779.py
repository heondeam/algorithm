from sys import stdin as s
from sys import maxsize
import heapq

s = open("input.txt", "rt")

""" 14002. 최소비용 구하기 2 """


def dijkstra(x):
    queue = []

    # 힙에 (현재 거리, 노드) 형식으로 푸쉬 (최소힙이므로 거리가 가장 짧은 것 부터 pop 된다.)
    heapq.heappush(queue, (0, x))

    # 시작 노드의 거리는 0
    distances[x] = 0

    while queue:
        # 현재 거리, 현재 노드
        d, v = heapq.heappop(queue)

        # 거리가 d보다 작다면? 볼 필요 없다.
        if distances[v] < d:
            continue

        # 인접한 노드들에 대해서 방문을 시작한다.
        for nw, nx in graph[v]:
            # 현재 노드 + 인접 노드까지의 거리
            nd = d + nw

            if distances[nx] > nd:
                heapq.heappush(queue, (nd, nx))
                route[nx] = v
                distances[nx] = nd


if __name__ == "__main__":
    # 도시의 개수
    n = int(s.readline().rstrip())
    # 버스의 개수
    m = int(s.readline().rstrip())
    # 버스 정보
    edges = [list(map(int, s.readline().rstrip().split())) for _ in range(m)]
    # 최소비용 과 경로를 구하고자 하는 출발 도시 -> 도착 도시
    s, e = list(map(int, s.readline().rstrip().split()))

    graph = []

    route = [s] * (n + 1)
    distances = [maxsize] * (n + 1)

    for i in range(n + 1):
        graph.append([])

    for edge in edges:
        sn, en, cost = edge

        graph[sn].append((cost, en))

    dijkstra(s)


    ans = []
    tmp = e
    while tmp != s:
        ans.append(tmp)
        tmp = route[tmp]
    
    ans.append(s)
    ans.reverse()

    # print(graph)
    print(distances[e])
    print(len(ans))
    print(*ans, sep=" ")
    # print(distances)